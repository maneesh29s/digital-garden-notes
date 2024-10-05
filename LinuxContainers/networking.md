---
aliases: []
author: Maneesh Sutar
date: 2024-09-01
tags: []
title: Networking in containers
---

# Networking in containers

## Network namespaces

 > 
 > In linux, each process by default inherits all the namespaces from its parent process

You can think of each network namespace **representing an isolated machine with its own network**. Each namespace will have a ==private set of IP addresses,== its own ==routing table==, socket listing, connection tracking table, firewall, ==own network interfaces== other network-related resources.  
So processes in different namespaces can have same IP range without any conflict. In such case the routing table in each namespace should handle packet route properly.

 > 
 > Each **network interface** (physical or virtual) is **present in exactly one namespace** and can be moved between namespaces.

Also, ==processes within the same network namespace can be thought of as running in the same host==, so they can talk to each other using `localhost`. This is possible because each new network namespace by default will have a **loopback interface**.

For 2 processes which are in different namespaces to talk to each, you need to create a `link` between the 2 network namespaces using `veth` pairs.

 > 
 > By default every time you start a new docker container, a new network namespace is created specific to the container.

To see all the network namespaces `sudo lsns -t net`  
This will show ==all the network interfaces accessible via the== `/proc` ==filesystem==  
So if you are running above command in a container which typically has its own isolated filesystem (via `mount` namespace), you might not see all the namespaces.  
But from host you will see namespaces of all the running containers too.

## Virtual Ethernet Pair (veth)

When you start a Docker container, Docker creates a pair of connected virtual Ethernet devices (a "veth" pair). One end of this pair is attached to the container as its network interface (usually `eth0` inside the container), and the other end is attached to the host's network namespace.

`sudo ip link add veth0 type veth peer name veth1`

This command creates two virtual network interfaces, `veth0` and `veth1`. These ==two interfaces are connected==, so packets sent to `veth0` will appear on `veth1` and vice versa.

To bring them up,

````bash
sudo ip link set dev veth0 up
sudo ip link set dev veth1 up
````

Docker typically ==sets namespaces for the virtual ethernet== inside a container.  
To create new network namspace,  
`ip netns add s1`

To set the namespace of the `veth0` (one end of the pair) to `s1` ,  
`ip link set veth0 netns s1`

To revert back the namespace of `veth0` to the "default" root namespace (initialised by `init` daemon)  
`sudo ip netns exec s1 ip link set veth0 netns 1`

To check all the network interfaces present in the network namespace of a process,  
`sudo nsenter -t <pid of the process> -n ip a`

## Bridge network interface

Acts as a virtual switch

To create a new bridge interface called `br0` run

````bash
sudo ip link add name br0 type bridge 
sudo ip link set dev br0 up
````

You can also assign IP range to the bridge using  
`sudo ip addr add 192.168.1.1/24 dev br0`

Following command adds `veth0` to the `br0` bridge interface, making `veth0` a port of the bridge.  
`sudo ip link set veth0 master br0`  
This will only connect `veth0` will become a port of the switch `br0` . All the frames (layer 2) from `veth0` will also reach `br0`, and from `br0` to any other virtual ethernets attached to it, depending on the MAC addresses.

Since switch is layer 2 device, it doesn't have to do anything with IP addresses.  
IP addresses have to be explicitly added using `sudo ip addr add`

To show all "link" between virtual interfaces and bridge networks (present in current network namespace)  
`bridge link show`

To see which veths are connected to a bridge interface `docker0`,  
\`brctl show docker0

When you create a new network using  `docker network create ...`, docker creates a new bridge interface.

### If bridge is at layer 2, why assign IPs to it?

Since bridge is a [switch](../ComputerNetworking/network_devices.md), it works at layer 2 of OSI. So its only concerned about the layer 2 properties (MAC addresses, MTU etc.) of  the devices connected to it.  Bridge can't do anything for layer 3 i.e. assigning IP, managing routes etc.

But ==bridges act as an helper to the docker daemon== for managing networking of the containers.  
**All the layer 3 things are handled by the docker daemon itself.** 

### Which layer 3 operations are handled by docker daemon?

* **Bridge network setup**: 
  
  * When a container is created and attached to a bridge network, Docker assigns it an IP address from the ==subnet allocated to that bridge== (e.g., `172.17.0.0/16` for the default bridge network). This is done by the Docker daemon itself.
  * Docker uses an internal **IPAM** (**IP Address Management**) system that keeps track of which IPs have been assigned and dynamically allocates an available IP from the subnet to the container. This happens when the container starts, and there is ==no separate DHCP service involved.==
  * The container receives its IP address, default gateway, and DNS configuration through a process that mimics DHCP but it is all handled by Docker's internal mechanisms without requiring a standalone DHCP server.
* **DNS Resolution**: 
  
  * For every container, Docker creates embedded DNS server, which runs inside the network namespace of the container (at some IP `127.0.0.x`). Containers connected to the Docker bridge network are automatically configured to use the embedded DNS server as their primary DNS resolver. 
  * ==Which DNS entries to add for each container depends on which bridge network that container is connected to==.
  * If the container is added to a new bridge, docker sends new entries in the container's DNS config.
* **NAT**:
  
  * Docker sets up `iptables` rules for both outbound masquerading and inbound port forwarding.
  * **IP masquerading** allows containers with private IP addresses to communicate with the outside world through the host’s IP.
  * **Port forwarding** allows inbound connections from the host to the container.

### Why docker uses bridge?

For containers to communicate with each other, **bridge** is really not necessary, since one end of `veth` pair is always present in the host namespace. Host will treat that end as any other network interface (like `eth0`). Adding correct route table entry will allow containers to send IP packets to each other, but TBH its going to be tedious.

So here are the advantages of bridge network:

1. **Logical isolation at layer 2 (link layer)**
   
   1. Bridge acts as a virtual switch at layer 2 of OSI.
   1. Even though one end of veth is in the host namespace, once we set a "master" bridge for veth, veth acts as ==one of the ports of the bridge==. In this case, ==the layer 2 "frames" from veth can only travel inside the bridge network==, and they can't reach the host without explicitly assigning IP route (layer 3). 
   1. Also, containers connected to different bridge networks are also isolated from each other at layer 2.
1. **Simplified connectivity between host and containers**
   
   1. Route table will only contain one entry corresponding to the bridge network. Without bridge, for every new container, host has to manually add route table entry.
   1. Bridge networks often work with [NAT](../ComputerNetworking/NAT.md) allowing containers to communicate with the external world (e.g., internet or host) while still being isolated from the host system.
   1. The bridge makes port forwarding simple, so containers can be accessed externally without exposing the entire host network.
1. **Changing the network** that a container is part of becomes easier because of the abstraction of a "bridge". Docker provides `docker connect` command to achieve the same.

1. **Access to Layer 2 functions** like mac address filtering, VLAN filtering, assigning priority 

## MACvlans and IPvlans

## References

1. <https://youtu.be/OU6xOM0SE4o>
1. <https://youtu.be/5grbXvV_DSk>
