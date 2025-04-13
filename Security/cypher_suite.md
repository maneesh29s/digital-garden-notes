---
aliases:
- Cypher Suites
author: Maneesh Sutar
created: 2024-05-31
modified: 2025-04-14
tags: []
title: Cypher Suite
---

# Cypher Suite

[Wiki](https://en.wikipedia.org/wiki/Cipher_suite)

Set of algorithms that help secure a network connection.

Suites typically use [Transport Layer Security](https://en.wikipedia.org/wiki/Transport_Layer_Security "Transport Layer Security")

## Contents of suite

**A suite contains**

1. Key exchange algorithm: [ECDHE](elliptical_curve_crypto.md#ECDH) , [RSA](rsa.md)
1. Digital signature (certificate) auth algorithms during handshake: [RSA](rsa.md), ECDSA
1. Symmetric encryption algorithm: [AES](aes.md), [ChaCha20](chacha.md)
1. Hash function for [HMAC](hashing.md#HMAC) and [HKDF](hashing.md#HKDF): [SHA](sha.md), MD5

## Support in TLS

Till TLS 1.2, multiple combination of cypher suites were supported such as

* ECDHE-RSA-AES256-GCM-SHA256
* ECDHE-ECDSA-AES128-SHA

From TLS 1.3, support for many of the existing cypher suites have been dropped. Also, the cypher suite now only contains

* the record protection (symmetric encryption) algorithm (including secret key length)
* a [hash](hashing.md) to be used with both the [HKDF](hashing.md#HKDF) and [HMAC](hashing.md#HMAC).

Example of TLS1.3 [cypher suites](https://datatracker.ietf.org/doc/html/rfc8446#appendix-B.4):

* TLS_AES_128_GCM_SHA256
* TLS_AES_256_GCM_SHA384
* TLS_CHACHA20_POLY1305_SHA256

Support for many of the legacy RSA based and DH algorithms were removed.  
It looks like TLS 1.3 is pushing towards to use of **elliptical curve** based algorithms, like ECDHE and ed25519 (EdDSA). TLS1.3 mandates [forward secracy](forward_secracy.md) for all connections.

Many popular sites now use [X25519](https://en.wikipedia.org/wiki/Curve25519) with AES_256_GCM as cypher suite.

See [this](https://datatracker.ietf.org/doc/html/rfc8446#section-4.2.3) for list of supported signature algorithm in the TLS 1.3  
Also see [this](https://datatracker.ietf.org/doc/html/rfc8446#section-4.2.7) for list of supported key exchange algorithms.
