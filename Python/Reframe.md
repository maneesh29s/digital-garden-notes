---
aliases: []
author: Maneesh Sutar
created: 2024-04-08
modified: 2024-09-28
tags: []
title: Reframe
---

# Reframe

[Documentation](https://reframe-hpc.readthedocs.io/en/stable/)

A **HPC regression testing** library

 > 
 > ReFrame is a powerful framework for writing system regression tests and benchmarks, specifically targeted to HPC systems.

Run tests with **different environments and systems easily**  
e.g. gnu + intel , clang + m1, gnu + amd, gnu + intel + nvidia

Environments and Systems are defined in python like config files (containing dictionaries)

Regression testing is an end-to-end testing of a system, where we are only concerned that

1. The program should correctly i.e. should produce correct output in different environments and systems
1. The performance of the system should improve OR stay the same as before
