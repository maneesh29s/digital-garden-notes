---
aliases: []
author: Maneesh Sutar
date: '2024-09-21'
tags: []
title: Network Devices
---


# Network Devices

> As far as I am concerned with

## Repeater

1. A dumb, 2 port output device
2. Works at physical layer (OSI layer 1)
3. Transmits data between 2 devices only

## Bridge

1. A slightly smarter [Repeater](#repeater)
2. Works at layer 1, has 2 ports, connects 2 devices
3. Can filter data based on mac addresses

## Hub

1. Works at Physical Layer i.e. OSI Layer 1
1. Contains multiple physical ports (assume multiple LAN cable points)
1. A **dumb** device, always broadcasts all data from one port to all other ports
1. No division of network
1. Only half-duplex transmission
1. For more info, visit [GFG](https://www.geeksforgeeks.org/what-is-network-hub-and-how-it-works/)

## Switches

1. Works at Data Link Layer i.e. OSI Layer 2
2. Switches can divide the network at data link layer using [VLANS](VLANS.md)
3. Smart, uses MAC ids to identify source and destination
4. Full duplex, controls bandwidth used by individual LANs
5. More info on [GFG](https://www.geeksforgeeks.org/what-is-a-network-switch-and-how-does-it-work/)

## Routers

1. Works at Network (IP) Layer i.e. OSI Layer 3
2. Divides network based on IP subnets
3. A layer 3 switch = Router with VLAN (layer 2) capabilities
4. More info on [GFG](https://www.geeksforgeeks.org/introduction-of-a-router/)

## Reference

1. <https://www.geeksforgeeks.org/network-devices-hub-repeater-bridge-switch-router-gateways/>
