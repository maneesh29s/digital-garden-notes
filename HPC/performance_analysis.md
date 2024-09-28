---
aliases: []
author: Maneesh Sutar
date: 2023-09-27
tags: []
title: Performance Analysis
---

# Performance Analysis

Specific to gcc compiled programs

## General

1. ALWAYS run with `-O3` enabled, even while debugging
1. Don't run with `-Ofast` as it replaces NaNs and inf with 0 and very large value
1. `-g` i.e. debug symbols DO NOT add any overhead to the program

## Performance Analysis Tools

[perf](https://man7.org/linux/man-pages/man1/perf.1.html): a command line performance analysis tool for linux. See [Brendan Gregg's Blogs](https://www.brendangregg.com/perf.html) for exmaples on how to use

[Nvidia Insight Systems](https://developer.nvidia.com/nsight-systems): a system-wide performance analysis tool designed to visualize an application’s algorithms, identify the largest opportunities to optimize, and tune to scale efficiently across any quantity or size of CPUs and GPUs

[Intel Advisor](https://www.intel.com/content/www/us/en/developer/tools/oneapi/advisor.html#gs.2wpz2k): design and analysis tool for developing performant code. The tool supports C, C++, Fortran, SYCL\*, OpenMP\*, OpenCL™ code, and Python

## Perf tools

````bash
# `-fno-omit-frame-pointer` : preserves stack trace
g++ -O3 -fno-omit-frame-pointer -g -o run app.cpp


# `-F99`: frequency of sampling, 99 Hz
# -g: preserve debug symbols (i think)
perf record -g -F99 ./run
# report is outputed in perf.data file


# by default reads from perf.data present in the same dir
# or you can specify the file with -i flag
perf report -g
````
