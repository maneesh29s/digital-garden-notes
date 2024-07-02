---
aliases:
- RSA
author: Maneesh Sutar
date: 2024-05-31
tags:
- public
title: RSA
---

# RSA

An [encryption](encryption.md) and [signature_authentication](signature_authentication.md) algorithm

Uses static public-private key.  
Data encrypted with public key can be decrypted with private key (and vice versa too)

Unlike [standard Diffie-Helman](dh.md), RSA does not provide [Forward Secrecy](forward_secracy.md), but it does provide [signature_authentication](signature_authentication.md), so we can make sure that the messages are being sent by the right party.  
In SSH, in remote server, we do this by adding the public keys of the client as **authorized_keys**, typically in a file `~/.ssh/authorized_keys`.

Over the internet however, RSA is still susceptible to [MITM](mitm.md) attacks. Thus websites use [TLS certificates](https://en.wikipedia.org/wiki/Public_key_certificate#) to verify the public key of the server.

In practice, ==RSA is almost never used as a key exchange mechanism==, because of lack of forward secrecy. In protocols like **SSH**,  ==it is only used as user authentication==, along with [ECDHE](dh.md) algorithms for the key-exchange. Nowadays SSH defaults to generate a [ed25519](dh.md#ECDSA) key for user authentication instead of RSA key.

RSA was used as user authentication algorithm in [Cypher Suites](cypher_suite.md) till TLS 1.2.  
==Since TLS 1.3, use of RSA is deprecated==, instead newer [ECDSA](dh.md#ECDSA) algorithms like [ed25519](dh.md#ECDSA) are preferred.

Nevertheless, the algorithm is interesting, so go give it a read.

## Basic Principle

A basic principle behind RSA is the observation that it is practical to find three very large positive integers e, d, and n, such that for all integers m (0 ≤ *m* \< *n*),

$$(m^e)^d \mod n = m \mod n$$

because the two exponents can be swapped,, **the private and public key can also be swapped**, allowing for message [signing and verification](signature_authentication.md) using the same algorithm.

## Key generation

Ref: <https://www.cs.utexas.edu/users/mitra/honors/soln.html>  
The math behind public-private key generation by Eddie Woo: [video](https://youtu.be/oOcTVTpUsPQ)

* Choose $p = 3$ and $q = 11$
* Compute $n = p*q = 3*11 = 33$
  * n is used as the [modulus](https://en.wikipedia.org/wiki/Modular_arithmetic "Modular arithmetic") for both the public and private keys. Its length, usually expressed in bits, is the [key length](https://en.wikipedia.org/wiki/Key_length "Key length").
  * n is released as part of the public key.
* Compute $\phi(n) = (p - 1)*(q - 1) = 2*10 = 20$.
  * To know about $\phi$ , refer the video above or see [Carmichael's totient function](https://en.wikipedia.org/wiki/Carmichael%27s_totient_function).)
* Choose $e$ such that $1 < e < \phi(n)$ and $e$ and $\phi(n)$ are co-prime. Let $e = 7$
* Compute a value for d such that $(d*e) \mod \phi(n) = 1$.  
  One solution is d = 3 ; as $(3*7) \mod 20 = 1$
* Public key is $(e, n) => (7, 33)$
* Private key is $(d, n) => (3, 33)$

To play around with RSA key generation, try python's [cryptography library](https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/).

## Encryption and Decryption

Both public and private keys are actually pair of 2 large integers

For now assume, on the receiver end,  
public key (e,n) = (5, 14)  
private key (d,n) = (11, 14)

note that n is same in both public-private key. See the [key generation](#key-generation)

message to be sent = 10

**Encryption**

Encrypted message = (message) ^ (e) mod (n)  
= $10 ^ 5 \mod 14$  
= 12

**Decryption**

message    = (encrypted message) ^ (d) mod (n)  
= $12 ^ {11} \mod 14$  
= 10

## Signing

The ==scope of signing is only to check whether sender really signed the document==.  
In such cases encryption is typically handled using other methods.

For signing, ==sender uses their public-private key pair==

On sender end, these are the keys

* Public key is (e, n) => (7, 33)
* Private key is (d, n) => (3, 33)

Message to be signed: "I signed" which converts to "14"

**Signing**  
Sender uses their **private key** to generate signature.  
sign = (message) ^ (d) mod n  
= 14 ^ 3 mod 33  
= 5

**Verification of the sign**  
Anyone who has the public key of sender can verify the signature.  
new_message = (sign) ^ 7 mod 33  
= 5 ^ 7 mod 33  
= 14

Since the new_message is as expected , signature is verified.

## Limitations

1. **RSA is used to encrypt messages that are shorter than the modulus of the public key.** For 1024-bit keys, this means that the message must be 117 bytes or fewer (the modulus is 128-bytes, minus 11 for the padding of the message).

1. The security of RSA relies on the practical difficulty of factoring the product of two large prime numbers, or the "[factoring problem](https://en.wikipedia.org/wiki/Factoring_problem "Factoring problem")". This solution to the problem is slow, but not as slow as a brute-force attack as there are algorithms available. Thus we need very large [key length](https://en.wikipedia.org/wiki/Key_size#). As per [this](https://en.wikipedia.org/wiki/Key_size#Asymmetric_algorithm_key_lengths),
   
   * 1024-bit RSA keys are equivalent in strength to 80-bit symmetric keys
   * 2048-bit RSA keys to 112-bit symmetric keys
1. RSA is **much slower due to its mathematical complexity**. It is not suitable for encrypting large data directly.

1. Unlike [Diffie–Hellman key exchange](dh.md), It does not provide [Forward Secrecy](forward_secracy.md)

## References

1. [RSA Operation](https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Operation)
1. RSA encryption by Eddie Woo: [video](https://youtu.be/4zahvcJ9glg)
1. RSA signing by Adam Clay [video](https://youtu.be/rLR8WcXy03Q)
