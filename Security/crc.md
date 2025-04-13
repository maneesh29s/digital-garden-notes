---
aliases:
- CRC
- CRC32
author: Maneesh Sutar
created: 2024-05-31
modified: 2025-04-14
tags: []
title: Cyclic Redunduncy Checks
---

# Cyclic Redundancy Checks

An [error detection](error_detection.md) scheme.

Using CRC algorithms, we can generate "check value", which are used to verify the integrity of the data.

Typically used during transport of data via network.  
The [network packet](https://en.wikipedia.org/wiki/Network_packet) contains CRCs to detect error during transmission.

## Working

Rather than me writing, best explained by these 2 references:

1. CRCs [youtube video](https://youtu.be/izG7qT0EpBw?si=r8NVkftzRnTAa3V7) by Ben Eater
1. [CRC Wiki's "Computation"](https://en.wikipedia.org/wiki/Cyclic_redundancy_check#Computation).
