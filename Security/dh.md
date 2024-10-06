---
aliases:
- Diffie-Hellman key exchange
- ECDH
- ECDHE
author: Maneesh Sutar
created: 2024-05-31
modified: 2024-09-28
tags: []
title: Diffie-Hellman key exchange
---

# Diffie–Hellman key exchange

**Diffie–Hellman key exchange or DH** is a mathematical method of securely exchanging cryptographic keys over a public channel.  
Used to generate a random symmetric secret key between any 2 hosts that wish to communicate securely.

Due to a new secret key used every session, this algorithm introduces [forward secracy](forward_secracy.md) in the system which pure RSA does not. But standard DH does not provide [user verification](signature_authentication.md), so there's no way to verify whether client/server had actually sent the message. Thus, it is highly susceptible to [MITM](mitm.md) attacks. Today standard DH is never used.

In TLS [Cypher Suites](cypher_suite.md), a version of DH called [ECDHE](#ecdh) is used for **key sharing**, and [ECDSA](#ecdsa) or [RSA](rsa.md) is used for [user authentication](signature_authentication.md).

## Types of keys

**Ephemeral:**

* temporary secret key
* provides [Forward Secrecy](forward_secracy.md)
* no [signature_authentication](signature_authentication.md) or authenticity

**static:**

* long term shared secret
* implicit authenticity (as it is guranteed that only the secret holder can encrypt the message)
* no forward secrecy

"**ephemeral, static**" or "**semi-static**":

* no forward secrecy
* one-sided authenticity

## Finite Field Diffie-Hellman

A [great animated video](https://youtu.be/85oMrKd8afY) on the working on DH algorithm.  
This is the working of the **standard Diffie-Hellman** algorithm, later formalized as **Finite Field Diffie-Hellman** algorithm

**Finite Field DH** has roughly the same key strength as [RSA](rsa.md#limitations) for the same key sizes.  
So 2048-bit FFDH has same security as 2048-bit RSA

To try hands-on with numbers, refer to python's [cryptography library](https://cryptography.io/en/latest/hazmat/primitives/asymmetric/dh/) documentation.

## ECDH

**Elliptic-curve Diffie–Hellman** or [ECDH](https://en.wikipedia.org/wiki/Elliptic-curve_Diffie%E2%80%93Hellman) encryption uses DH key exchange, and [elliptical curve](https://en.wikipedia.org/wiki/Elliptic-curve_cryptography) method to generate the secret.  
Have a look at this [youtube video](https://youtu.be/NF1pwjL9-DE) to understand the math.

Elliptical curves ==allow smaller keys to provide equivalent security==, compared to cryptosystems based on modular exponentiation such as [RSA](rsa.md) or even the standard Diffie Helman.

But a **256-bit ECDH** key has approximately the same safety factor as a 128-bit [aes](aes.md) key (which is even higher than 2048 bit RSA)

**ECDHE** (where final 'E' stands for "ephemeral") and its variants like [X25519](https://en.wikipedia.org/wiki/Curve25519) are widely used in TLS [cypher suite](cypher_suite.md) for initial key exchange.

Python's cryptography library has a seperate implementation of [X25519 key exchange](https://cryptography.io/en/latest/hazmat/primitives/asymmetric/x25519/)

## ECDSA

**Elliptical Curve Digital-Signature Algorithms** is a family of [Digital Signing and Authentication](signature_authentication.md) algorithms based on Elliptical curve cryptography.

[Ed25519](https://en.wikipedia.org/wiki/EdDSA#Ed25519) is an implementation of **ECDSA** (or [EdDSA](https://en.wikipedia.org/wiki/EdDSA#) to be specific) used widely for user authentication, like in **ssh**. It is also based on [Curve25519](https://en.wikipedia.org/wiki/Curve25519).  
To try hands-on of Ed25519 signing, refer python's cryptography module [documentation](https://cryptography.io/en/latest/hazmat/primitives/asymmetric/ed25519/)
