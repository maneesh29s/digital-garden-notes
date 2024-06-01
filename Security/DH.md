---
aliases:
- Diffie-Hellman key exchange
- ECDH
- ECDHE
author: Maneesh Sutar
date: 2024-05-31
tags:
- public
title: Diffie-Hellman key exchange
---

# Diffie–Hellman key exchange

**Diffie–Hellman key exchange or DH** is a mathematical method of securely exchanging cryptographic keys over a public channel.
Used to generate a random symmetric secret key between any 2 hosts that wish to communicate securely.

Due to a new secret key used every session, this algorithm introduces [forward secracy](forward_secracy.md) in the system which pure RSA does not.

But DH does not provide [sign and verify](signing.md), so there's no way to verify whether client/server had actually sent the message. Thus, it is highly susciptable to [MITM](mitm.md) attacks, where middleman generates separate secret keys with both client and server using the DH process, so it can encrypt and decrypt all the traffic.

In TLS [Cypher Suites](cypher_suite.md), a version of DH called [ECDH](#ecdh) is used for key sharing, and [RSA](rsa.md) is used for [signing and authentication](signing.md)

## Types of keys

**Ephemeral:**

* temporary secret key
* provides [Forward Secrecy](forward_secracy.md)
* no [signing](signing.md) or authenticity

**static:**

* long term shared secret
* implicit authenticity (as it is guranteed that only the secret holder can encrypt the message)
* no forward secrecy

"**ephemeral, static**" or "**semi-static**":

* no forward secrecy
* one-sided authenticity

## Finite Field Diffie-Hellman

This is the working of the **standard Diffie-Hellman** algorithm, later formalized as **Finite Field Diffie-Hellman** algorithm

![video](https://youtu.be/85oMrKd8afY?list=TLPQMzEwNTIwMjTjX8y6dMupBg)

**Finite Field DH** has roughly the same key strength as [RSA](rsa.md#limitations) for the same key sizes.
So 2048-bit FFDH has same security as 2048-bit RSA

## ECDH

**Elliptic-curve Diffie–Hellman** or [ECDH](https://en.wikipedia.org/wiki/Elliptic-curve_Diffie%E2%80%93Hellman) encryption uses DH key exchange, and [elliptical curve](https://en.wikipedia.org/wiki/Elliptic-curve_cryptography) method to generate the secret.

Elliptical curves allow smaller keys to provide equivalent security, compared to cryptosystems based on modular exponentiation such as [RSA](rsa.md).

But a **256-bit ECDH** key has approximately the same safety factor as a 128-bit [AES](AES.md) key (which is even higher than 2048 bit RSA)

**ECDHE** (where final 'E' stands for "ephemeral") and its variants like [Curve25519](https://en.wikipedia.org/wiki/Curve25519) are widely used in TLS [cypher suite](cypher_suite.md) for initial key exchange.
