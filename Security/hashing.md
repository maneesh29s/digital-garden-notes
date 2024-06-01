---
aliases:
- Hashing
author: Maneesh Sutar
date: 2024-05-31
tags:
- public
title: Hashing
---

# Hashing

Irreversible, one way computation
Original data can not be recovered from the hash
Uses math and prime numbers

In terms of security
bcrypt/argon > [SHA](sha.md) > [CRC32](CRC.md)

in terms of speed
[CRC32](CRC.md) > sha > bcrypt/argon

[SHA](sha.md): One of the oldest hashing algorithm. But today more secure algorithms are available. Today it is used check file integrity.

[CRC32](CRC.md): Faster than SHA, used in networking to verify if correct bits were received

Argon/bcrpyt: Purposefully slow to make cracking difficult. Used to store passwords.
