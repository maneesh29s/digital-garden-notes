---
aliases: []
author: Maneesh Sutar
date: 2024-01-12
tags: []
title: JIT in python
---

# JIT in python

Numba is one of the libraries which provide just-in time compilation for python

Examples: <https://people.duke.edu/~ccc14/sta-663-2016/18C_Numba.html>

Also python3.13 has added [JIT compiler](https://tonybaloney.github.io/posts/python-gets-a-jit.html)

Python is usually called an interpreted language, however, it combines compiling and interpreting. When we execute a source code (a file with a .py extension), Python first compiles it into a bytecode. The bytecode is a low-level platform-independent representation of your source code, however, it is not the binary machine code and cannot be run by the target machine directly. In fact, it is a set of instructions for a virtual machine which is called the Python Virtual Machine (PVM)  
Refer:

1. <https://dev.to/marvintensuan/is-python-interpreted-or-compiled-on-doubling-down-and-semantics-6gf>
1. <https://towardsdatascience.com/understanding-python-bytecode-e7edaae8734d>
1. <https://youtu.be/I4nkgJdVZFA>
