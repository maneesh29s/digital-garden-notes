---
aliases:
- CUB
author: Maneesh Sutar
created: 2023-11-29
modified: 2024-09-28
tags: []
title: NVIDIA CUB
---

# NVIDIA CUB

[Github repo](https://github.com/NVIDIA/cub)

Reusable software components for every layer of the CUDA programming mode

When working with GPUs, CPU creates a queue of operations to be run on GPU

in JAX, XLA uses cub to fuse(compose) operations together, so overhead of changing operations in threads is reduced

Based on easyness of programming:

ptax \< cuda \<  cub \< thrust
