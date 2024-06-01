---
aliases:
- Signing
author: Maneesh Sutar
date: 2024-05-31
tags:
- public
title: Authentication and Signing
---

# Authentication and Signing

Used to verify that the message received during communication was really sent by the author as intended.

A [MITM](mitm.md) may not read an encrypted message, but it can definitely alter the bits so that receiver will not receive the correct message.
If using [diffie hellman](DH.md) key exchange, the MITM can actually impersonate both client and server using different secret keys.

With signing, even if the data is corrupted during transport, the receiver will know that this is not the original data.

[RSA](rsa.md) along with Hashing algorithms like [SHA](sha.md) is used for signing a message
