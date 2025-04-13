---
aliases: []
author: Maneesh Sutar
created: 2024-06-11
modified: 2025-04-14
tags: []
title: Dask
---

# Dask

## Documentation

[link](https://docs.dask.org/en/stable/)

## Tutorials

NCAR tutorials: [link](https://github.com/NCAR/dask-tutorial?tab=readme-ov-file)

## Computation

Dask is **lazily evaluated**. The result from a computation isn’t computed until you ask for it. Instead, a Dask task graph for the computation is produced.

Anytime you have a Dask object (df, array) and you want to get the result, call `compute`
