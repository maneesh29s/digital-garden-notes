---
aliases:
- Encryption
- Asymmetric Encryption
- Symmetric Encryption
author: Maneesh Sutar
created: 2024-05-31
modified: 2025-04-01
tags: []
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
  * In [Diffie–Hellman key exchange](dh.md) the modulus, base and the public key (intermediate key) is known
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

### Block Cipher

[AES](aes.md) is a block cipher, it takes a block of fixed length of bits (128 or 256) and generates same number of bits in the output.  
The math going on while encrypting each block is kind independent of the other blocks. So all the blocks can be encrypted/decrypted parallelly.  
Even if one of the bits in a block are flipped, the integrity of the entire block of bits is compromised.

### Stream Cipher

Useful for streaming data e.g.  telephonic calls, steaming videos.  
[ChaCha](chacha.md) is a family of stream cipher algorithms.

Since encryption of each bit is dependent on the current state of the cipher, it is also known as **state cipher**.

The sequence of data is important, plus the speed is at paramount.  
In such cases, block ciphers might not be suitable, as the usecase "streaming" can not work efficiently on fixed "blocks" of data.

In Stream Ciphers, a key is used to generate a very long stream of pseudo-random bits, which is XORed with the data (thus flipping the bits) to encrypt/decrypt it.

Stream ciphers typically execute at a higher speed than block ciphers and have lower hardware complexity. However, stream ciphers can be susceptible to security breaches (see [stream cipher attacks](https://en.wikipedia.org/wiki/Stream_cipher_attack "Stream cipher attack")); for example, when the same starting state (seed) is used twice.
