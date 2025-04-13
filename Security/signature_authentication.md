---
aliases:
- Signing
author: Maneesh Sutar
created: 2024-05-31
modified: 2025-04-14
tags: []
title: Authentication and Signing
---

# Digital Signature and Authentication

Used to verify that the message received during communication was really sent by the author as intended.

[Public key DSA](encryption.md#Asymmetric) like [RSA](rsa.md) or [Ed25519](elliptical_curve_crypto.md#Ed25519) are used in protocols like TLS and SSH as the user authentication mechanisms.

In case of SSH, the public key of the client can be stored as "authorized keys" in the server, which is stored in `~/.ssh/authorized_keys` file.  
Thus, the server can verify the identity of a client, and [MITM impersonation](mitm.md) attacks can be prevented.

But over the internet, it is impossible to store authorized keys of all the clients in the world.  
In such cases, the server publishes its public key to the world, and its job of the client to verify that the public key is valid.

Thus, TLS uses [Digital Certificates](https://en.wikipedia.org/wiki/Public_key_certificate#) in standard formats lie [x_509](x_509.md) which are assigned to each website / organisations / server by some [Certificate Authority](pki.md#Certificate-Authority)  
A digital certificate primarily contains:

* the public key and information about it
* information about the identity of its owner or **subject**
* the digital signature of the certificate authority
