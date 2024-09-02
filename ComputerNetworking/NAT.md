---
aliases:
- NAT
- Network Address Translation
- PAT
author: Maneesh Sutar
date: 2024-08-20
tags:
- public
title: Network Address Translation
---

# Network Address Translation

## What is NAT?

**Network Address Translation (NAT)** is a method used by routers to ==allow multiple devices on a local (private) network to share a single public IP address== when accessing the internet.

NAT modifies the IP addresses in the header of IP packets as they pass through the router. NAT is commonly used in home and small business networks.

## Types of NAT

1. **Static NAT:**
   * Maps a specific private IP address to a specific public IP address.
   * This type of NAT is one-to-one; for every internal IP, there is a unique external IP.
1. **Dynamic NAT:**
   * Maps a private IP address to a public IP address from a pool of public IP addresses.
   * The mapping is temporary and can change over time.
1. **PAT (Port Address Translation) or Overloading:**
   * A type of dynamic NAT that maps multiple private IP addresses to a single public IP address but ==differentiates them by using different port numbers==.
   * This is the ==most common== type of NAT and is used in most home networks.

## Does PAT breaks OSI model?

We think that OSI layers should be clearly seperated out, each layer independent of other in any protocol.  
But NAT kind of breaks this assumption, since NAT depends on Network and TCP layer for its working.  
Also, NAT changes the perceived IP address of the client (sender). If the server (receiver) application depends on the actual IP of the sender, it might break since actual IP is hidden. In such case, the sender must send its actual IP in the "data" part of the packet.

## References

1. Good video summarizing everything: [Network Address Translation - Computerphile](https://www.youtube.com/@Computerphile)
1. [Wiki](https://en.wikipedia.org/wiki/Network_address_translation)
