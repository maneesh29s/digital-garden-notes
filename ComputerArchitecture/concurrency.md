---
aliases:
- Concurrency
author: Maneesh Sutar
created: 2023-07-14
modified: 2025-04-14
tags:
- concurrent
- computer-architecture
title: Concurrency
---

# Concurrency

## Why concurrent?

* **Any modern computer handles multiple tasks simultaneously:** e.g. generating GUI, running background processes, taking input from keyboard/mouse, network calls etc.
* For I/O intensive (disk read/write) tasks, with proper schedueling, the intermittent time can be spent to do something else. The same applies to virtually every I/O, even computations carried out on the GPU.

To know more about [io_flavours](../IO/io_flavours.md)

## Further Read

Read #todo

<https://blog.risingstack.com/concurrency-and-parallelism-understanding-i-o>

<https://penberg.org/blog/parallel.html#concurrency-and-parallelism>
