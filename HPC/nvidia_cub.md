---
aliases:
- CUB
author: Maneesh Sutar
date: 2023-11-29
tags:
- tofix
- public
title: NVIDIA CUB
---

# NVIDIA CUB

[Github repo](https://github.com/NVIDIA/cub)

reusable software components for every layer of the CUDA programming mode

When working with GPUs, CPU creates a queue of operations to be run on GPU

in JAX, XLA uses cub to fuse(compose) operations together, so overhead of changing operations in threads is reduced

Based on easyness of programming:

ptax \< cuda \<  cub \< thrust
