---
aliases: []
author: Maneesh Sutar
created: 2024-06-10
modified: 2025-04-14
tags: []
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

## Comparision to HDF5

The Hierarchical Data Format version 5 [HDF5](https://github.com/HDFGroup/hdf5) is also an open source file format.

In summary, both Zarr and HDF5 are very similar,

1. directory and files based structure
1. Each file containing multi-dimensional arrays
1. Metadata for each file/directory  
   And one can achieve same things with both Zarr and HDF5

**The benefit of Zarr**

1. Its relatively modern, supports things like using Json files for metadata (instead of binary files in HDF5), using semantic versioning for each file etc.,
1. extending `zarr-python` with custom filters/storage backends is relatively easy than extending HDF5, where everything is in C. Even for H5py (python wrapper over main HDF5 library), extension plugins must be written in C.
1. **HDF5 is single-threaded**. For parallel access, one must use MPI (or multi-processing). The `zarr-python` supports multi-thread access.

Reference: [https://youtu.be/-l445lCPTts](https://youtu.be/-l445lCPTts)
