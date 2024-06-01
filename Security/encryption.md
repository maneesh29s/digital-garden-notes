---
aliases:
- Encryption
- Asymmetric Encryption
- Symmetric Encryption
author: Maneesh Sutar
date: 2024-05-31
tags:
- public
title: Encryption
---

# Encryption

To protect the data to be sent over a network

Like a lock and key mechanism

Data can be recovered (decrypted) if the reciver holds the appropriate key

## Asymmetric

* Also known as [public key cryptography](https://en.wikipedia.org/wiki/Public_key_cryptography "Public key cryptography")

* Use public and private key pairs, one to encrypt and one to decrypt

* All such algorithms involve something information which is known publicly
  
  * In [RSA](rsa.md) the public key is known to everyone
  * In [Diffie–Hellman key exchange](DH.md) the modulus, base and the public key (intermediate key) is known
* Their effectiveness depends on the intractability (computational and theoretical) of certain mathematical problems such as [integer factorization](https://en.wikipedia.org/wiki/Integer_factorization "Integer factorization").
  
  * These problems are time-consuming to solve, but usually **faster than trying all possible keys by brute force**.
  * Thus, asymmetric keys must be longer for equivalent resistance to attack than symmetric algorithm keys. ([Refer](https://en.wikipedia.org/wiki/Key_size#Asymmetric_algorithm_key_lengths))
  * Also, this is why **asymmetric key algorithms are much slower than symetric key.**
* Asymmetric key algorithms are not commonly used to directly encrypt user data. More often, they is used to transmit shared keys for symmetric key cryptography, which are then used for bulk encryption–decryption.

* One of the major use cases of assymetric keys is [Digital signatures](https://en.wikipedia.org/wiki/Digital_signature "Digital signature"), in which a message is signed with the sender's private key and can be verified by anyone who has access to the sender's public key

## Symmetric

* Single shared key between both sender and receiver
* Same key used to encrypt and decrypt the data
* Symmetric key algorithms typically use Asymmetric algorithms for the secret key exchange
* symmetric-key encryption algorithms are usually better for bulk encryption
* They have a smaller key size, which means less storage space and faster transmission.
* e.g. [AES](AES.md)
