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
bcrypt/argon > [SHA](sha.md) > [CRC32](crc.md)

in terms of speed  
[CRC32](crc.md) > sha > bcrypt/argon

[SHA](sha.md): One of the oldest hashing algorithm. But today more secure algorithms are available. Today it is used check file integrity. It is used in [HMAC](#hmac)

[CRC32](crc.md): Faster than SHA, used in networking (at network layer) to verify if correct bits were received. CRCs are easily reversible.

Argon/bcrpyt: Purposefully slow to make cracking difficult. Used to store passwords.

## HMAC

[Wiki](https://en.wikipedia.org/wiki/HMAC)

**Hash-based Message Authentication Codes** typically use any cryptographic hash functions like [SHA-2](sha.md) to generate the message authentication code.

Idea is to use the split the secret shared key (typically the symmetric key in encryption) in 2 subkeys, and compute hashes twice using those subkeys + plain text.   
At the receiving end, the hash is recalculated using the shared secret key and the decrypted plain text. If the hash matches the HMAC passed along with the cipher text, then the message is authenticated.

Since TLS 1.3, **HMAC** is not used, instead new encryption schemes like [AES GCM](aes.md#AES-GCM) and [ChaCha20-Poly1305](chacha.md) are used which provide [authenticated encryption with associanted data (AEAD)](https://en.wikipedia.org/wiki/Authenticated_encryption#Authenticated_encryption_with_associated_data)
