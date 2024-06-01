---
aliases:
- Hamming Codes
author: Maneesh Sutar
date: 2023-09-01
tags:
- public
title: Error Correction
---

# Error Correction

## Concepts

[Hamming Distance and MHD](hamming_distance.md)

**Redundancy (bits**): Additional bits that we send with our data

**Block length** = Message Length + Redundancy bits length

**Rate** = Message Length / Block length

**ECC Notation**: (Message block size, data bits size, hamming distance)

Number of bit-errors which are **detectable** = MHD - 1

Number of bit-error which are **correctable** = floor ( (MHD - 1) / 2 )

## Why error correction? isn't detection enough?

Think about deep space communication where transmission time is in hours  
Re-transmission is time consuming and costly

## Why correction and detection together is not possible?

Take example of [Hamming Codes](#hamming-codes) (HC) which have [Hamming Distance](hamming_distance.md) of 3.

Even though HC can detect 2 bit errors, it cannot distinguish

* a double bit error of some valid code
* a single bit error of a different valid code  
  It won't be sure which is the "right" codeword to convert to.

Similarly, in Extended HC, with hamming distance of 4, triple errors might get mistaken for single errors and "corrected" to the wrong value.

So your system can either choose to detect the errors, or correct the errors.

# Error Correction Schemes

## Repetition

Data is repeated $r$ times  
e.g. say $r = 3$

|Data|Output|
|----|------|
|0|000|
|1|111|
|0110|000 111 111 000|

**Notation:**  
$$[r, 1, r]$$

Hamming distance  = $r$  
Block length = $r$  
Message length = 1

For r = 3, repetition provides 1 bit error correcting OR 2 bit error detection

## Hamming Codes

Play around with hamming codes using [playground](https://docs.google.com/spreadsheets/d/1eYzlwtUPrevD95FoAhPIt2A6nAkIjm6YOprlPqGR5zw/edit?usp=sharing)

**Notation:**  
$$[2r − 1, 2r − r − 1, 3]$$

Here $r$ is a natural number >= 2  
Hamming Distance = 3  
Block length = $2r − 1$  
Message length = $2r − r − 1$

**Hamming codes** (irrespective of $r$) provide either

* 1 bit error correcting
* 2 bit error detecting

**Why MHD is 3 ?**  
In hamming codes, for a single bit flipped in the data part, 2 parity bits corresponding to that bit location also need to be flipped in order for the overall code to be a valid hamming code.

For a data bit going from 0 to 1, total 3 (the data bit and 2 parity bits) bits are flipped.  
This is true for all hamming code schemes (7,4 or 15,11 or others), because in each case the way the parity bit works are same.

## Extended Hamming Codes

**Notation**  
$$[2r − 1, 2r − r − 1, 3]$$

Here "r" is a natural number >= 2  
Hamming Distance = 4  
Block length = 2r − 1  
Message length = 2r − r − 1

**Extended Hamming codes** always provide either

* 1 bit error correcting AND upto 2 bit guaranteed error detecting
* 3 bit error detecting

**Why MHD is 4?**  
In the extended hamming codes, an extra parity bit is added to existing scheme (15,11 -> 16,11), which contains the parity of the entire block.  
This makes hamming distance 4 (check yourself with the [playground](https://docs.google.com/spreadsheets/d/1eYzlwtUPrevD95FoAhPIt2A6nAkIjm6YOprlPqGR5zw/edit?usp=sharing))

## Extended Binary Golay code

Notation:  
$$[24, 12, 8]$$

Block length: 24  
Message length: 12  
Hamming Distance: 8  
Rate = 12/24 = 0.5

Since Hamming Distance = 8, this scheme provides either

* Error Correction upto 3 bits
* Error Detection upto 7 bits

## Reed–Solomon error correction

Notation:  
$$[n, k, n − k + 1]$$

One of the scheme is $[255, 223, 33]$ with hamming distance of 33.

Applications: Data Storage (CDs, DVDs), Barcodes, Space Transmission
