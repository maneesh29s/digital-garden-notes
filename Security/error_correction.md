---
aliases: null
author: Maneesh Sutar
date: 2023-09-01
tags:
- tofix
- public
title: Error Correction
---

# Error Correction

## Why error correction? isn't detection enough?

Think about deep space communication where transmission time is in hours
Re-transmission is time consuming and costly

## Concepts

**Hamming Distance**: difference between bitwise positions of 2 code words

**Min hamming distance (MHD)**: min. number of bits that need to be flipped for the next valid code word

**Redundancy (bits**): Additional bits that we send with our data

**Block length** = Message Length + Redundancy bits length

**Rate** = Message Length / Block length

**ECC Notation**: (Message block size, data bits size, hamming distance)

Number of bit-errors which are **detectable** = MHD - 1

Number of bit-error which are **correctable** = floor ( (MHD - 1) / 2 )

## Methods for Error Correction

### Repetition

Data is repeated "r" times

say r = 3
0: 000
1: 111

0110: 000 111 111 000

Hamming distance  = r
Block length = r
Message length = 1
Rate: 1 / r
Notation: (r, 1, r)

1 bit error correcting OR 2 bit error detecting

### Hamming Codes

<https://docs.google.com/spreadsheets/d/1eYzlwtUPrevD95FoAhPIt2A6nAkIjm6YOprlPqGR5zw/edit?usp=sharing>

Here "r" is a natural number >= 2

Hamming Distance = 3
Block length = 2r − 1
Message length = 2r − r − 1
Rate:
Notation \[2r − 1, 2r − r − 1, 3\]2-code

1 bit error correcting OR 2 bit error detecting

### Extended Hamming Codes

Here "r" is a natural number >= 2

Hamming Distance = 4
Block length = 2r − 1
Message length = 2r − r − 1
Rate:
Notation \[2r − 1, 2r − r − 1, 3\]2-code

1 bit error correcting AND upto 2 bit guranteed error detecting
OR 3 bit error detecting

### Extended Binary Golay code

\[24, 12, 8\]

Block length: 24
Message length: 12
Hamming Distance (HD): 8

Rate = 12/24 = 0.5

Since HD = 8,
Error Detection =  7 bits ( 8 - 1)
Error Correction = 3 ( 2\*3 + 1 \< 8)

### Reed–Solomon error correction

\[n, k, n − k + 1\]

e.g. (255, 223, 33)

Applications: Data Storage (CDs, DVDs), Barcodes, Space Transmission
