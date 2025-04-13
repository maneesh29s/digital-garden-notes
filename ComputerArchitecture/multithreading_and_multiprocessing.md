---
aliases:
- Multithreading and Multiprocessing
- Multithreading
- Multiprocessing
author: Maneesh Sutar
created: 2023-11-18
modified: 2025-04-14
tags: []
title: Multithreading and Multiprocessing
---

# Multithreading and Multiprocessing

Pre-requisites: [Processes and Threads](program_processes_threads.md) and [multi_cpu_and_multi_core_systems](multi_cpu_and_multi_core_systems.md)

## Multithreading

A program runs in a single process which can spawn multiple threads.

OS can schedule these threads for [concurrent](./concurrency.md) execution using scheduling.

It might be possible for each thread to be executed simultaneously on a separate cores of a [multi-core CPU](multi_cpu_and_multi_core_systems.md), though it depends on the implementation of multithreading library / programming language.  
**e.g**. Python does not allow parallel execution of threads belonging to single process. For more info check [here](../Python/Multithreading_vs_Multiprocessing_in_python.md). C++, Java allows it.

Since threads share virtual memory address space with the parent process, multi-threading is only possible in **shared memory** architecture, like a multi-core CPU.  
Additionally, we need to make use locking mechanisms to prevent multiple threads from writing to the same memory location simultaneously.

Multithreading libraries in c++: [openmp](https://www.openmp.org/), std::thread

## Multiprocessing

Same program runs across more than one processes.  
Such processes do not share virtual memory address space, so they can be run either on a **distributed memory** architecture, like a [multi-cpu system](multi_cpu_and_multi_core_systems.md).

On a **shared memory** architecture, the OS takes care of separating the virtual address space. The OS can also schedule each process to be executed on different cores of a [multi-core CPU](multi_cpu_and_multi_core_systems.md).

Code and data memory is different for each process, so no locking mechanism required.

In order share data from one process to another, we need to use **In-process communication** like [MPI](https://www.mpi-forum.org/).

Multiprocessing libraray in c++: [openmpi](https://www.open-mpi.org/)

## Multithreading + Multiprocessing

In this case, same program run in multiple processes, each process spawning multiple threads.

In C++, possible to implement using openmpi and openmp/std::threads together.
