---
aliases:
- Network Aggregation
- Bonding
author: Maneesh Sutar
created: 2023-12-11
modified: 2025-04-14
tags: []
title: Network Aggregation
---

# Network Aggregation

<https://en.wikipedia.org/wiki/Link_aggregation>

Also known as **Bonding**

Using multiple interfaces instead of single to increase throughput  
Also provides redunduncy against failure

Aggregation can occur at any level of OSI model (Physical, Data Link or Network)

## Linux drivers

The Linux *bonding* driver provides a method for aggregating multiple NICs into a single logical bonded interface of two or more so-called *(NIC) slaves*.

### Modes for the Linux bonding driver

**Round-robin (balance-rr)**

Transmit alternate [network packets](https://en.wikipedia.org/wiki/Network_packet "Network packet") ==in sequential order from the first available== NIC slave through the last.

**XOR (balance-xor)**  
Transmit network packets ==based on a hash of the packet's source== and destination.

**Broadcast (broadcast)**  
Transmit ==network packets on all slave network== interfaces. This mode provides fault tolerance.

**IEEE 802.3ad Dynamic link aggregation (802.3ad, LACP)**  
Creates aggregation groups that ==share the same speed and duplex settings==. Utilizes all slave network interfaces in the active aggregator group according to the 802.3ad specification. This mode is similar to the XOR mode above and supports the same balancing policies. The link is set up dynamically between two LACP-supporting peers.
