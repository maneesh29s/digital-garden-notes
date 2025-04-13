---
aliases:
- ECDSA
- Elliptical Curve Cryptography
author: Maneesh Sutar
created: 2025-03-31
modified: 2025-04-13
tags: []
title: Elliptical Curve Cryptography
---

# Elliptical Curve Cryptography

Wiki: [elliptical curve](https://en.wikipedia.org/wiki/Elliptic-curve_cryptography)

Elliptical curves ==allow smaller keys to provide equivalent security==, compared to cryptosystems based on modular exponentiation such as [RSA](rsa.md).  
A **256-bit ECDH** key has approximately the same safety factor as a 128-bit [aes](aes.md) key (which is even higher than 2048 bit RSA)

In TLS, Elliptical Curve Cryptography is used primarily for:

1. Key Exchange: Generating a shared secret which later form the symmetric key
1. [Certificate Signing and Verfication](signature_authentication.md): Used to verfiy authenticity of the server using [Public Key Infrastructure](pki.md) and [X.509](x_509.md) certificates

 > 
 > Elliptical Curve Cryptography on its own **can not be** used for encryption and decryption. Instead, its always paired with [Symmetric Encryption](encryption.md) algorithms in cypher suites.

## The math

Have a look at this [youtube video](https://youtu.be/NF1pwjL9-DE) to understand the math.

**In summary:**

1. The machine generates a random 32 byte number which becomes the **private key (pk)**.
1. The **generator function (G)**  is determined based on:
   1. The curvature (e.g. prime256v1, curve25519)
   1. Other curve parameters if any
1. The **public key (P)** is derived using the formula: $$P = pk \cdot G$$  
   **Notes:**
1. The function **G** and public key **P** are part of the **public information** during any elliptical curve based algorithm.
1. Public key can be derived from private key, but **vice-versa is impossible.**
1. Unlike RSA, the public and private keys are **not interchangable**.

## ECDH

**Elliptic-curve Diffie–Hellman** or [ECDH](https://en.wikipedia.org/wiki/Elliptic-curve_Diffie%E2%80%93Hellman)  uses DH key exchange, and [Elliptical Curve Cryptography](elliptical_curve_crypto.md) method to generate the secret.

**ECDHE** (where final 'E' stands for "ephemeral") schemes like [X25519](https://en.wikipedia.org/wiki/Curve25519) are widely used in TLS [cypher suite](cypher_suite.md) for initial key exchange. Python's cryptography library has a seperate implementation of [X25519 key exchange](https://cryptography.io/en/latest/hazmat/primitives/asymmetric/x25519/)

### General algorithm:

Let's assume a scenario where 2 systems, A and B wish to communicate securely, for which they need to generate a shared secret using ECDH.

1. A creates random private key ($pk_A$), selects elliptical curve parameters which determines generation function $G$, and generates public key ($P_A$) using the formula: $$P_A = pk_A . G$$
1. A sends the $P_A$ and information about elliptical curve params to B.
1. B also generates its own random private key ($pk_B$). It uses the ellptical curve params from A to get the same generation function $G$, and computes its own public key $P_B$: $$P_B = pk_B . G$$
1. B sends its public key $P_B$ to A.
1. Finally, similar to standard [Diffie-Hellman key exchange](dh.md), the shared secret is the private key multiplied with the public key of other system.  
   $$shared\_secret = pk_A . P_B = pk_B . P_A = pk_A . pk_B . G $$

## ECDSA

**Elliptical Curve Digital-Signature Algorithms** is a family of Digital Signing and Authentication algorithms based on Elliptical curve cryptography..

### Ed25519

[Ed25519](https://en.wikipedia.org/wiki/EdDSA#Ed25519) is an implementation of **ECDSA** (or [EdDSA](https://en.wikipedia.org/wiki/EdDSA#) to be specific) used widely for user authentication, like in **ssh**. It is based on [Edward Curves](https://en.wikipedia.org/wiki/Twisted_Edwards_curve).

To try hands-on of Ed25519 signing, refer python's cryptography module [documentation](https://cryptography.io/en/latest/hazmat/primitives/asymmetric/ed25519/)

For detailed explaination of Algorithm, visit [this note](ed25519.md)
