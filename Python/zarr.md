---
aliases: []
author: Maneesh Sutar
date: 2024-06-10
tags:
- public
title: Zarr
---

# Zarr

[tutorial](https://zarr.readthedocs.io/en/stable/tutorial.html#tutorial)  
More learnings are present in the [jupyter notebook](https://github.com/maneesh29s/digital-garden/blob/main/notebooks/zarr.ipynb)

Zarr is a format for the storage of chunked, compressed, N-dimensional arrays inspired by HDF5.

## Key things

1. Supports in-memory and persistent arrays with no change in the API
1. Stores data in chunks, **operates on chunks**. Can work on large arrays without memory being full.
1. Zar arrays have their own functions as replacement for commonly used numpy features
1. **Supports multi-threading and multi-processing**
1. Supports multiple storage formats e.g. zip, LMDB, Reddis, AWS S3, HDFS

## Basic Usage

````python
import zarr

zarr.create() // empty array
zarr.zeros() // zero filled array

zarr.open() // disk persisted empty array

zarr.save() // to save in-memory zar array to disk
zarr.load() // load disk persisted array to memory
````

## Performance

On Ryzen 9 5900X with 64 GB RAM

Data = 1D array of 2^30 64-bit elements, uncompressed size: 8.58 GB

Using 1D data as parquet does not support 2D data

‌

### With random data

**Using Parquet:**

Time to write: 24.9 seconds

Size on disk:  8.3 GB

Notes: Single threaded, written to a single data.parquet file.

**Using Zarr:**

Time to write: 4.7 seconds

Size of disk: 7.1 GB

Note: Multi threaded with 8 threads, around 200% total CPU usage. Data written to 1024 seperate files (2^20 elements per file)

‌

### With sequential data

Using Parquet:

Time to write: 27.7 seconds

Size on disk:  4.3 GB

Notes: Single threaded, written to a single data.parquet file.

‌

Using Zarr:

Time to write: 1.9 seconds

Size of disk: 51MB

Note: Multi threaded with 8 threads, around 200% total CPU usage. Data written to 1024 seperate files (2^20 elements per file)
