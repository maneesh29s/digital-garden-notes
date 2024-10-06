---
aliases: []
author: Maneesh Sutar
created: 2023-06-04
modified: 2024-09-28
tags: []
title: Oblivious Algorithms
---

# Oblivious Algorithms

[Oblivious](../Dictionary/Oblivious-(en-US).md) algorithms's control flow is independent of some properties (value , size) of the input data.  
Quick sort (or merge sort, or any adaptive sorting) are non-oblivious, because the algorithm steps change based on data.  
[Bitonic Sort](https://en.wikipedia.org/wiki/Bitonic_sorter) (also known as sorting net) is oblivious, because **it always compares the same elements disregarding data it gets**  
Bitonic sort does exactly the same steps in the best and the worst case, while non-oblivious algorithms may vary from $n$ steps to $n^2$ (for example).

## Algorithm Design Strategy

||adaptive|oblivious|
|--|--------|---------|
|control flow|complex|simple|
|raw compute|less|more|
|support parallel processsing|maybe|yes|
|best suited for|CPU|GPU|

Control Flow: conditionals, loops

GPUs can't handle complex control flows, but they can perform 1000x raw calculations (because of parallelisation) than CPUs

## Types of Oblivious Algorithms

### Cache Oblivious Algorithm

An algorithm which is [Oblivious](../Dictionary/Oblivious-(en-US).md) to cache size

e.g. [FunnerSort](https://en.wikipedia.org/wiki/Funnelsort)

To learn more, have a look at this [video lecture](https://www.youtube.com/watch?v=xwE568oVQ1Y)
