---
aliases:
- Memory Banking
- Interleaved Memory
author: Maneesh Sutar
created: 2024-01-11
modified: 2024-09-28
tags: []
title: Memory Banking
---

# Memory Banking

My understanding after going through [this video](https://youtu.be/CDOOxhRBMIY?list=PL5Q2soXY2Zi-EImKxYYY1SZuGiOAOBKaf&t=4882) and the "Chapter 2: Memory Hierarchy Design" in Computer Architecture book:

1. [Interleaved Memory](https://en.wikipedia.org/wiki/Interleaved_memory) is a general concept which is used in both RAMs and Processor Caches, in which the memory addresses are evenly speed across **multiple banks**.

1. Since the addresses are spread evenly, the consecutive elements in an array are (ideally) stored in separate memory banks. This is particularly useful for vector load/store instructions, since in a single instruction, the CPU is aware that it needs to fetch/store 4/8 elements from the memory. This can be easily pipelined, and reading/writing at these addresses can achieve a rate of 1 element per cycle.

1. Memory Banks are actually part of the DRAM chip itself. DRAM chips are commonly sold on small boards called dual inline memory modules (DIMMs) (our typical RAM). DIMMs typically contain 4 to 16 DRAMs, each DRAM having its own memory bank

1. The *double data rate (DDR)* technology in DRAMs increases bandwidth by transfering data on both the rising edge and falling edge of the DRAM clock signal. This is different concept than banking.
