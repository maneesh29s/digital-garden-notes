---
aliases: []
author: Maneesh Sutar
created: 2024-10-20 19:00:00
modified: 2024-11-30
tags:
- todo
title: Python JIT performances
---

# Python JIT performances

Various JIT compilers available for python that I know of are:

1. [numba](https://github.com/numba/numba)
1. [jax](https://github.com/jax-ml/jax) but is very specifically made to boost numpy-like operations
1. Alternative interpreters like [pypy](pypy.md)

## Performance between approaches

Note: #todo  Compare performance between

1. pure `CPython`
1. Cython [C-extension](python_and_c.md)  + `CPython`
1. `numba + CPython`
1. `pypy`

Goal of the benchmarking will be to do minimal change to the original pure python function, and see the performance difference.

For reference codes:

https://www.cardinalpeak.com/blog/faster-python-with-cython-and-pypy-part-2 , code is at https://bitbucket.org/tom_craven/cython_test/src/master/?filedownload=https://bitbucket.org/tom_craven/

https://neurohackweek.github.io/cython-tutorial/04-numba/
