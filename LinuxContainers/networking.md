---
aliases: []
author: Maneesh Sutar
date: 2024-09-01
tags:
- public
title: Networking in containers
---

# Networking in containers

## Virtual Ethernet Pair (veth)

When you start a Docker container, Docker creates a pair of connected virtual Ethernet devices (a "veth" pair). One end of this pair is attached to the container as its network interface (usually `eth0` inside the container), and the other end is attached to the host's network namespace.

`sudo ip link add veth0 type veth peer name veth1`

This command creates two virtual network interfaces, `veth0` and `veth1`. These ==two interfaces are connected==, so packets sent to `veth0` will appear on `veth1` and vice versa.

By default, a new process inherits namespaces from its parents.  
Docker typically ==sets namespaces for the virtual ethernet== inside a container.   
To create new network namspace,  
`ip netns add s1`

To set the namespace of the `veth0` (one end of the pair) to `s1` ,  
`ip link set veth0 netns s1`

## Bridge network interface

Acts as a virtual switch  
Other virtual interfaces connect to bridge, and they can inherit network settings like IP range from the bridge interface

`sudo ip link set veth0 master br0`  
This command adds `veth0` to the `br0` bridge interface, making `veth0` a port of the bridge.

To show all bridge interfaces,  
`bridge link show`

To see which veths are connected to a bridge interface `docker0`,  
\`brctl show docker0

When you create a new network using  `docker network create ...`, docker creates a new bridge interface.

Although bridge interfaces (like `docker0`) can act as regular virtual ethernets, ==docker does not attach containers directly to the bridge interfaces== created by it,  due to:

1. **Network Isolation:** 
1. **Flexibility:** By using a veth pair, ==Docker can easily connect containers to different network namespaces, bridges, or even overlay networks== without needing to modify the container or the host's network interfaces.
1. **Scalability:** This model allows Docker to manage multiple containers on a host, each with its own isolated network stack, while still allowing communication through the `docker0` bridge or other Docker networks.

## MACvlans and IPvlans

## References

1. https://youtu.be/OU6xOM0SE4o
1. https://youtu.be/5grbXvV_DSk
