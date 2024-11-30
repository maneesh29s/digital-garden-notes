---
aliases: []
author: Maneesh Sutar
created: 2024-10-20 18:45:00
modified: 2024-10-20
tags: []
title: Python and C
---

# Python and C

1. `ctypes` in-built python module can be used to call functions from compiled shared libraries i.e. ABI level. Documentation is good. An [article](https://asiffer.github.io/posts/numpy/#introduction) to get started.
1. CFFI is also a python code which works at [ABI or API](https://cffi.readthedocs.io/en/stable/goals.html) (C source code) level. See [repo](https://github.com/python-cffi/cffi?tab=readme-ov-file).
1. [Cython](https://cython.org/) is a programming language with very python-like syntax, but it has types annotation and ==can directly call C functions from standard library==, like we do in usual C language. **Cython is a also compiler** which generates C code from valid cython code, then compiles C code to a shared library (lib.so), which can be directly imported to regular python code. But because of the way Cython compiler works, the library support for Cython is limited, so might not work all the time.
1. [swig](../CPP/swig.md) can also be used, did not explore yet.
1. Finallyl, writing direct [Python](https://docs.python.org/3/extending/extending.html) / [Numpy C API](https://numpy.org/doc/stable/reference/c-api/array.html) is as low-level as you can get, but needs effort to write native C code.

## Bonus: Python and C++

1. [pybind11](https://github.com/pybind/pybind11) : Simple and lightweight. Uses newer C++ features.
1. [Boost-python](https://www.boost.org/doc/libs/1_85_0/libs/python/doc/html/index.html) : In the game for long time, but heavy, because of boost.
