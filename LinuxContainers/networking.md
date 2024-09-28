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

By default, a new process inherits namespaces from its parents.  
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
This will only connect `veth0-veth1` to `br0` . So all the packets from `veth0` will also reach `br0`, and from `br0` to any other virtual ethernets attached to it, depending on the IP and route configuration.  
Note that above command will not assign IP address to the veth pair.  
IP addresses have to be explicitly added using `sudo ip addr add`

To show all "link" between virtual interfaces and bridge networks (present in current network namespace)  
`bridge link show`

To see which veths are connected to a bridge interface `docker0`,  
\`brctl show docker0

When you create a new network using  `docker network create ...`, docker creates a new bridge interface.

Although bridge interfaces (like `docker0`) can act as regular virtual ethernets, ==docker does not attach containers directly to the bridge interfaces== created by it,  due to:

1. **Network Isolation**
1. **Flexibility:** By using a veth pair, ==Docker can easily connect containers to different network namespaces, bridges, or even overlay networks== without needing to modify the container or the host's network interfaces.
1. **Scalability:** This model allows Docker to manage multiple containers on a host, each with its own isolated network stack, while still allowing communication through the `docker0` bridge or other Docker networks.

## MACvlans and IPvlans

## References

1. <https://youtu.be/OU6xOM0SE4o>
1. <https://youtu.be/5grbXvV_DSk>
