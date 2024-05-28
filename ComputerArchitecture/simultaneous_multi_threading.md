---
aliases:
- SMT
- Simultaneous multithreading (SMT)
author: Maneesh Sutar
date: 2024-01-08
tags:
- public
title: Simultaneous multithreading (SMT)
---

# Simultaneous multithreading (SMT)

[Wiki](https://en.wikipedia.org/wiki/Simultaneous_multithreading#)
Paper:  [Converting thread-level parallelism to instruction-level parallelism via simultaneous multithreading](https://dl.acm.org/doi/10.1145/263326.263382)

==SMT permits multiple independent threads of execution== to better use the resources provided by modern CPU core.

Issue multiple instructions from multiple threads in one cycle. ==The processor must be== [superscalar](superscalar_processor.md) to do so.

[Hyper-threading Technology](intel_x86_64_architecture.md) is intel's implementation of SMT.
From Intel's SDM Vol 1 section 2.2.8:

 > 
 > Each logical processor executes instructions from an application thread using the resources in the processor core. The core executes these threads concurrently, using out-of-order instruction scheduling to maximize the use of execution units during each clock cycle.

AMD Zen architecture processors also support SMT.
