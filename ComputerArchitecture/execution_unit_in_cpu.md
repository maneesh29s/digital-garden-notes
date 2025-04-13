---
aliases:
- Execution Unit
- Functional Unit
author: Maneesh Sutar
created: 2024-01-10
modified: 2025-04-14
tags: []
title: Execution Unit
---

# Execution Unit

Also referred to as **Functional Unit** in "Computer-Architecture-patterson-5th-edition.pdf"

A Functional Unit is the ==smallest unit in a CPU which can perform some operations==

Examples of Execution Units are:

1. ALU: Integer Add, Mul, Shift
1. FP: Floating point Add, Mul
1. SIMD: Vector add, mul, shift
1. Load and Store

Inside a core of a processor, there can be multiple copies of above execution units. In such cases, the processor can be termed as [Superscalar Processor](superscalar_processor.md)

## References

1. [Wiki](https://en.wikipedia.org/wiki/Execution_unit)
1. [Execution Units in Intel Haswell](https://www.realworldtech.com/haswell-cpu/4/)
