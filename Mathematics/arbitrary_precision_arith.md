---
aliases: []
author: Maneesh Sutar
created: 2024-03-30
modified: 2024-09-28
tags: []
title: Arbitrary-precision arithmetic
---

# Arbitrary-precision arithmetic

From [wiki](https://en.wikipedia.org/wiki/Arbitrary-precision_arithmetic#):  
In computer science, arbitrary-precision arithmetic, also called bignum arithmetic, multiple-precision arithmetic, or sometimes infinite-precision arithmetic, indicates that **calculations are performed on numbers whose digits of precision are limited only by the available memory of the host system**.  
This contrasts with the faster fixed-precision arithmetic found in most arithmetic logic unit (ALU) hardware, which typically offers between 8 and 64 bits of precision.

Examples of such libraries:

1. [GMP](https://gmplib.org/): GNU Multiple Precision Arithmetic Library. [Wiki](https://en.wikipedia.org/wiki/GNU_Multiple_Precision_Arithmetic_Library). GMP is a free library for arbitrary precision arithmetic, operating on **signed integers, rational numbers, and floating-point numbers**. There is no practical limit to the precision except the ones implied by the available memory in the machine GMP runs on. GMP has a rich set of functions, and the functions have a regular interface.
1. [mpmath](https://mpmath.org/): Python library for real and complex floating-point arithmetic with arbitrary precision. mpmath internally uses Python's builtin long integers by default, but automatically switches to [GMP](http://gmplib.org/)/[MPIR](http://www.mpir.org/) for much faster high-precision arithmetic if [gmpy](http://code.google.com/p/gmpy) is installed. See [doc](https://mpmath.org/doc/current/basics.html#basic-usage) for usage.

## Reference

1. <https://en.wikipedia.org/wiki/Arbitrary-precision_arithmetic#>
