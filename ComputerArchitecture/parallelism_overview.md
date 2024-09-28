---
aliases: []
author: Maneesh Sutar
date: 2023-03-25
tags: []
title: Overview of Parallelism
---

# Overview of Parallelism

## Kinds of parallelisms in Computer Application

On a very high level, parallelism in applications is categorised as

### Data Level Parallelism (DLP)

* arises when ==multiple data items need to be operated== upon at the same time

### Task-Level Parallelism (TLP)

* arises when ==multiple tasks need to be run== simultaneously and independently

## How computer hardware exploits the parallelisms?

### Instruction-level parallelism (ILP)

* exploits data-level parallelism at modest levels with compiler help using ideas like pipelining and at medium levels using ideas like speculative execution
* Internal to hardware, not accessible to programmers
* Micro-architectural techniques that are used to exploit ILP include:
  * [Instruction pipelining](https://en.wikipedia.org/wiki/Instruction_pipelining "Instruction pipelining")
  * [Superscalar](superscalar_processor.md) execution, [VLIW](https://en.wikipedia.org/wiki/Very_long_instruction_word "Very long instruction word"), and the closely related [explicitly parallel instruction computing](https://en.wikipedia.org/wiki/Explicitly_parallel_instruction_computing "Explicitly parallel instruction computing")
  * [Out-of-order execution](https://en.wikipedia.org/wiki/Out-of-order_execution "Out-of-order execution")
  * [Register renaming](https://en.wikipedia.org/wiki/Register_renaming "Register renaming")
  * [Speculative execution](https://en.wikipedia.org/wiki/Speculative_execution "Speculative execution")
  * [Branch prediction](https://en.wikipedia.org/wiki/Branch_prediction "Branch prediction")
* [Simultaneous multithreading (SMT)](simultaneous_multi_threading.md) converts thread-level parallelism to instruction-level parallelism

### Vector Architectures and GPUs

* exploit **DLP** parallelism by applying a single instruction to a collection of data in parallel
* examples of vector architectures: SSE, AVX, NEON, RISCV-V

### Thread-level parallelism

* exploits either **DLP** or **TLP**
* possible to use in hardware which support interaction among threads
* using libraries like [OpenMP](https://passlab.github.io/OpenMPProgrammingBook/Ch2_MulticoreMultiCPU.html) or manually writing fork/join modelled programs  programmer can create multiple threads which can run simultaneously on a [Multicore systems](multi_cpu_and_multi_core_systems.md)

### Request-level parallelism

* parallelism among largely decoupled tasks specified by programmer
* I don't consider this as some low level thing
* e.g. client sending multiple independent requests to a remote server simultaneously

## Reference

1. David A. Patterson and John L. Hennessy. 1990. Computer architecture: a quantitative approach. Morgan Kaufmann Publishers Inc., San Francisco, CA, USA.
