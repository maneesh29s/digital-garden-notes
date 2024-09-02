---
aliases: []
author: Maneesh Sutar
date: 2024-09-02
tags:
- public
title: Linux Networking Commands
---

# Linux Networking Commands

## ip

### ip link

Manage network devices

### ip route

Manipulate routing table entries.

The output of the `ip route` command may look like this:

`192.168.5.0/24 dev eth0 proto kernel scope link src 192.168.5.1 metric 100`

This line represents a routing rule in the IP routing table of your system. Let's break down each part:

1. **`192.168.5.0/24`**

* **Meaning:** This specifies the destination network for the route. The `192.168.5.0/24` notation refers to the IP address range `192.168.5.0` to `192.168.5.255`.
* **Details:** The `/24` indicates a subnet mask of 255.255.255.0, meaning the first 24 bits are the network part of the IP address, and the last 8 bits can vary to represent host addresses within that network.

2. **`dev eth0`**

* **Meaning:** This tells the system to use the network interface `eth0` to reach the `192.168.5.0/24` network.
* **Details:** `eth0` is the network interface on your system that is connected to this subnet.

3. **`proto kernel`**

* **Meaning:** This indicates that the route was added by the kernel automatically, rather than by a user or a static configuration.
* **Details:** Typically, routes are automatically added by the kernel when an IP address is assigned to an interface.
* "proto dhcp" means route was added when ip was assigned by dhcp server

4. **`scope link`**

* **Meaning:** The scope of the route is `link`, meaning it is valid only for directly connected hosts on the same link (i.e., the local network).
* **Details:** This is typical for directly connected subnets where no intermediate routing is needed to reach the destination.

5. **`src 192.168.5.1`**

* **Meaning:** This specifies the source IP address to be used when sending packets to the `192.168.5.0/24` network.
* **Details:** `192.168.5.1` is the IP address assigned to the `eth0` interface on your system. When sending packets to the `192.168.5.0/24` network, this address will be used as the source address.

6. **`metric 100`**

* **Meaning:** The metric value represents the cost of using this route. Lower values indicate preferred routes.
* **Details:** A metric of `100` is a relative cost associated with this route. If there are multiple routes to the same destination, the one with the lowest metric will be chosen.

## bridge and brctl

To manage bridge interfaces

## References

1. https://www.redhat.com/sysadmin/7-great-network-commands
