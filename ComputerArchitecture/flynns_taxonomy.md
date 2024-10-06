---
aliases:
- Flynn's Taxonomy
author: Maneesh Sutar
created: 2024-05-27
modified: 2024-09-28
tags: []
title: Flynn's Taxonomy
---

# Flynn's Taxonomy

## Single Instruction stream, Single Data stream (SISD)

* uniprocessor
* looks like standard sequential computer, but internally can exploit **Instruction-level parallelism (ILP)**

## Single Instruction stream, Multiple Data stream (SIMD)

* same instructions executed by multiple processors on different data streams
* here "processor" does not mean a different physical CPU or another thread, "processor" is a smallest unit which can process data.
* Each processor has its own data memory (hence the MD of SIMD), but there is a single instruction memory and control processor

## Multiple Instruction streams, Single Data stream (MISD)

* No commercial multiprocessor of this type available

## Multiple Instruction streams, Multiple Data stream (MIMD)

* Each process fetches its own instructions, and operates on its own data
* more expensive than **SIMD**

## References

Read #todo

1. <https://penberg.org/blog/parallel.html>
