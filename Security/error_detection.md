---
aliases: []
author: Maneesh Sutar
date: 2023-09-01
tags:
- tofix
- public
title: Error Detection
---

# Error Detection

## repetition

10101110 10101110 10101110 10101110 10101110

## parity - minimum hamming distnace of 2

odd 1: 1
even 1: 0

10101110 1 valid

10101010 1 invalid

10100010 1 valid

10000010 1 invlid

00000010 1 valid

minimum hamming distance = d
number of bit errors that you can detect = d - 1

## Checksum

10101110 10101110 10101110 10101110 01000111

10101110
10101110
10101110
10101110
00000000
01000111

------------
10 10110110

10110110
00000010

---------

11111111

## CRC - cyclic redunduncy check

[CRC](CRC.md)

## finite field

Associativity

(a + b) + c = a + (b + c) =

Commutativity
a + b = b + a

-a = 0 - a

1 + 1 = 0
1 - 1 = 0
0 - 1 = 1
