---
aliases:
- Diffie-Hellman key exchange
- ECDH
- ECDHE
author: Maneesh Sutar
created: 2024-05-31
modified: 2025-04-14
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

## ECDH(E)

In this, [Elliptical Curve Cryptography](elliptical_curve_crypto.md) is used to perform the DH key exchange.  
This is more secure than Finite Field DH, and most widely in [TLS](tls.md)  
Please refer to the [ECDH](elliptical_curve_crypto.md#ECDH)
