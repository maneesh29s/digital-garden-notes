---
aliases:
- Programming Model
- Execution Model
author: Maneesh Sutar
date: 2024-03-02
tags:
- GPU
- public
title: Programming Model
---

# Programming Model

Refers to how **a programmer expresses code**

e.g. Sequential (SISD on von neuman), Data Parallel using special vector instructions (SIMD), Multi-threaded programs (MIMD, SPMD)

Refer [Flynn's Taxonomy](flynns_taxonomy.md)

# Execution Model

Refers to **how the underlying hardware exeutes the code**

e.g. Out-of-order execution, Vector Processor, Array Processor, Multi-core processor, Multi-processor

Refer [parallelism_overview](parallelism_overview.md)

# Different Scenarios

Execution model can differ from programming model  
e.g. Sequential code executed in OoO fashion by a superscalar processor

|Programming Model|Possible Execution|
|-----------------|------------------|
|SISD|Processor with ILP ; OoO execution ; VLIW processor|
|SIMD|Array or Vector (pipelined) processing units|
|SPMD|Multi-core / Multi-processor systems ; SIMD processors (GPU)|
