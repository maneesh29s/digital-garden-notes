---
aliases: []
author: Maneesh Sutar
created: 2024-10-20 19:32:00
modified: 2024-11-30
tags: []
title: pypy
---

# pypy

Repo: https://github.com/pypy/pypy  
Docs: https://doc.pypy.org/en/latest/

**An alternative interpreter** for python with JIT compilation  
You can run your pure python files, but instead of `python` interpreter, you run `pypy` interpreter.

 > 
 > Today I found out that the usual `python` command we are used to run on any machine, is in reality the **CPython** interpreter. CPython is the "reference" and default and mostly-used, but its not the only interpreter in python ecosystem.

Performance of pure python with pypy significantly faster.

But some modules like Numpy, Scipy call CPython C API extensions, where pypy may cry to run the python code, because those C APIs are not meant to be run on a different interpreter like pypy.

Best way to know about these things is read their [FAQ](https://doc.pypy.org/en/latest/faq.html#frequently-asked-questions)

Install pypy using their official website, as newer versions support python 3.10.

Conda-forge has older builds, and they recently dropped support for pypy train because of maintainence overhead.
