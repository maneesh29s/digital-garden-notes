---
aliases: []
author: Maneesh Sutar
created: 2023-10-26
modified: 2025-04-14
tags:
- AcceleratedComputing
- GPU
title: GPGPU Programming
---

# GPGPU Programming

This page talks about various programming techniques by which users can write general purpose code which executes on the GPU.

## By NVIDIA

### CUDA

Nvidia [CUDA](https://docs.nvidia.com/cuda/cuda-c-programming-guide) was launched in 2006.  
This allowed users to use GPUs for more general purpose applications than just rendering the graphics.

CUDA is as low as you can get, so the best performance is achieved in this.

### CCCL

[Github repo](https://github.com/NVIDIA/cccl)

"CUDA Core Compute Libraries" is a collection of **header-only** C++ libraries, which (from [README](https://github.com/nvidia/cccl?tab=readme-ov-file)) "provide general-purpose, speed-of-light tools to CUDA C++ developers, allowing them to focus on solving the problems that matter".

Basically provides abstraction over CUDA.

This was a unification of 3 libraries which were previously present in seperate repos:

1. [Thrust](https://github.com/NVIDIA/cccl/tree/main/thrust): Provides C++ functions for various operations (mathematical, algorithms like sort). These functions are called from `host` code of C++ program.
1. [CUB](https://github.com/NVIDIA/cccl/tree/main/cub) : A set of lower-level CUDA specfic C++ functions. These are called inside the `device` code of C++ program (i.e. inside the kernel)
1. **libudacxx**: CUDA C++ Standard Library. It provides an implementation of the C++ Standard Library that works in both host and device code.

### MatX

[Github](https://github.com/NVIDIA/MatX)

NVIDIA/MatX is a **C++17** library for numerical computing.  
It provides an API closer to Numpy or Cupy, but in C++.

## Python

1. [C++ Thrust](https://nvidia.github.io/cccl/thrust/)
1. [python cupy](https://cupy.dev/)

## Allowing Tensor programming

### Numerical Computations

1. [Python JAX](../Python/JAX.md)

### More focused on ML application

1. Tensorflow
1. Pytorch
