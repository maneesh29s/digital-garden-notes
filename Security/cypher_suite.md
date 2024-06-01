---
aliases:
- Cypher Suites
author: Maneesh Sutar
date: 2024-05-31
tags:
- public
title: Cypher Suite
---

# Cypher Suite

[Wiki](https://en.wikipedia.org/wiki/Cipher_suite)

Set of algorithms that help secure a network connection.

Suites typically use [Transport Layer Security](https://en.wikipedia.org/wiki/Transport_Layer_Security "Transport Layer Security") 

## Contents of suite

**A suite contains**

1. a key exchange algorithm: [ECDHE](DH.md#ECDH) , [RSA](rsa.md)
1. authentication algorithm during handshake: [RSA](rsa.md), ECDSA
1. block encryption algorithm: [AES](AES.md)
1. message authentication algorithms: [SHA](sha.md), MD5

## Support in TLS

Till TLS 1.2, multiple combination of cypher suites were supported such as

* ECDHE-RSA-AES256-GCM-SHA256
* ECDHE-ECDSA-AES128-SHA

From TLS 1.3, support for many of the existing cypher suites have been dropped. Currently most dominantly used protocol is

* [X25519](https://en.wikipedia.org/wiki/Curve25519) (ECDH) with AES_256_GCM
