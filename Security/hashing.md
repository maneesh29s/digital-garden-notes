---
aliases:
- Hashing
author: Maneesh Sutar
created: 2024-05-31
modified: 2024-09-28
tags: []
title: Hashing
---

# Hashing

## General Idea

Irreversible, one way computation, which ==convert a message to a hashed value==  
Original message should not be recoverable from the hashed value  
Hashed value ==should be unique for the given message==. This means that even a single bit flip in the original message should change the hashed value completely.  
Uses modulo mathematics and prime numbers.

## Comparison of some hash functions

 > 
 > Although [CRC](crc.md) are not categorised as "hash" functions, they are also used for maintaining the integrity of the message during network transport.

|Category|[CRC32](crc.md)|[SHA](sha.md)|Bcrypt/Argon2|
|--------|-----|---|-------------|
|Security against known attacks|Lowest|Medium|Highest|
|Computation|Fastest|Medium|Slowest|

[SHA](sha.md): One of the oldest hashing algorithm. In TLS it is used is used as hashing mechanism for [HMAC](#hmac). It is also used to check file integrity after downloading from internet.

[Argon](https://en.wikipedia.org/wiki/Argon2)/Bcrypt: Purposefully slow to make cracking difficult. Used to store passwords.

## HMAC

[Wiki](https://en.wikipedia.org/wiki/HMAC)

**Hash-based Message Authentication Codes** typically use any cryptographic hash functions like [SHA-2](sha.md) to generate the message authentication code.

Idea is to use the split the secret shared key (typically the symmetric key in encryption) in 2 subkeys, and compute hashes twice using those subkeys and the message.

At the receiving end, the hash is recalculated using the shared secret key and the message. If the hash matches the HMAC passed along with the cipher text, then the message is authenticated.

Now, depending on "what constitutes a message", there can be 3 ways in which HMAC is calculated: ([Reference](https://moxie.org/2011/12/13/the-cryptographic-doom-principle.html))

1. **Mac And Encrypt** : The sender computes a MAC of the plaintext, encrypts the plaintext, and then appends the MAC to the ciphertext. Ek1(P) || MACk2(P). ==Not recommended.==
1. **Mac Then Encrypt** : The sender computes a MAC of the plaintext, then encrypts both the plaintext and the MAC. Ek1(P || MACk2(P))
1. **Encrypt Then Mac** : The sender encrypts the plaintext, then appends a MAC of the ciphertext. Ek1(P) || MACk2(Ek1(P)).

As per the above [reference](https://moxie.org/2011/12/13/the-cryptographic-doom-principle.html) article, "**Encrypt then Mac**" is the best option, since you don't have to decrypt the cipher text before checking the authenticity of the message.

Since TLS 1.3, **HMAC** is not used, instead new encryption schemes like [AES-GCM](aes.md#AES-GCM) and [ChaCha20-Poly1305](chacha.md) are used which provide [authenticated encryption with associanted data (AEAD)](https://en.wikipedia.org/wiki/Authenticated_encryption#Authenticated_encryption_with_associated_data). Both AES-GCM and ChaCha20-Poly1305 internally use a version of "Encrypt then Mac" scheme to generate the "Authentication Tag" along with the cipher text.

## HKDF

**HMAC-based Key Derivation Function (HKDF)** is a standard algorithm in [TLS Cypher Suites](cypher_suite.md) used to derive a fixed length [symmetric key](encryption.md) from a secret.

The secret is either

* A pre-shared key ([PSK](https://en.wikipedia.org/wiki/Pre-shared_key))
* A shared secret, which is generated between 2 parties using [Diffie-Hellman key exchange](dh.md)

HKDF is the composition of two functions, **HKDF-Extract** and **HKDF-Expand**  
Read [wiki](https://en.wikipedia.org/wiki/HKDF#Mechanism) to learn how it works.
