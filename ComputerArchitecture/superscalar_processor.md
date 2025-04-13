---
aliases:
- Superscalar Processor
author: Maneesh Sutar
created: 2024-01-10
modified: 2025-04-14
tags: []
title: Superscalar Processor
---

# Superscalar Processor

<https://en.wikipedia.org/wiki/Superscalar_processor>

Detailed Paper: <https://courses.cs.washington.edu/courses/cse471/01au/ss_cgi.pdf>

A superscalar processor is a CPU that implements a form of parallelism called [Instruction-Level Parallelism](parallelism_overview.md)

In contrast to a scalar processor, which can execute at most one single instruction per clock cycle, ==a superscalar processor can execute more than one instruction during a clock cycle== by simultaneously dispatching multiple instructions to different [Execution Unit](execution_unit_in_cpu.md) on the processor.

Each [Execution Unit](execution_unit_in_cpu.md) is not a separate processor (or a core if the processor is a multi-core processor), but an execution resource within a single CPU such as an int ALU, FP, SIMD, load/store.
