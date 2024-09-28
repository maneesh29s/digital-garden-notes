---
aliases:
- Hamming Distance
- Minimum Hamming Distance
- MHD
author: Maneesh Sutar
date: 2024-06-01
tags: []
title: Hamming Distance
---

# Hamming Distance

==The number of bit positions where two codes differ==

e.g.  
1010 and 1100 : 3  
1010 and 1011: 1  
1010 and 1111 : 2

# Minimum Hamming Distance

In a ==given system of valid code words==, it is the ==minimum number of bit positions where any two VALID code words differ==

e.g.  
Suppose in a system of data transmission, ==for error detection, each bit is repeated thrice==.  
Thus, a data (code word) is valid, only if each of its bits are repeated thrice

Original data: 010  
Sent data: 000111000  
Original data: 011  
Sent data: 000111111

By flipping 1 bit in original data, 3 bits are flipped in the valid code word  
Try adding more bits to original data, minimum 3 times more bits will be added to a valid data.

Thus the minimum hamming distance is 3.

Number of bit-errors which are **detectable** = MHD - 1  
Number of bit-error which are **correctable** = floor ( (MHD - 1) / 2 )
