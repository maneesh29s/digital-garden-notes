---
aliases: []
author: Maneesh Sutar
date: 2024-05-31
tags: []
title: Security
---

# Folder: Security

**Purpose**

1. To protect data from getting in the hands on unauthenticated users
1. To preserve integrity of the data during transport

````mermaid
flowchart TD


%% Variable Definitions

SECURITY[Security]

ENCRYPTION["<a class='internal-link' href='./encryption'>Encryption</a>"]

ERROR_DETECTION["<a class='internal-link ' href='./error_detection'>Error Detection</a>"]

SIGN_AUTH["<a class='internal-link' href='./signature_authentication'>Signing and Authentication</a>"]

RSA["<a class='internal-link' href='./rsa'>RSA</a>"]

X25519["<a class='internal-link' href='./dh#ECDH'>X25519</a>"]

ARGON_BCRYPT[Argon2/Bcrypt]

SHA["<a class='internal-link' href='./sha'>SHA</a>"]

CRC["<a class='internal-link' href='./crc'>CRC</a>"]

ED25519["<a class='internal-link' href='./dh#ECDSA'>ed25519</a>"]

ERROR_CORRECTION["<a class='internal-link' href='./error_correction'>Error Correction</a>"]

  

SYMMETRIC[Symmetric Encryption]

ASYMMETRIC[Asymmetric Encryption]

AES_GCM["<a class='internal-link' href='./aes'>AES-GCM</a>"]

CHACHA["<a class='internal-link' href='./chacha'>ChaCha20-Poly1305</a>"]

HASHING["<a class='internal-link' href='./hashing'>Hashing</a>"]

X509_CERT["<a class='internal-link' href='./x_509'>X.509</a>"]

  

%% Grouping related nodes with subgraphs

subgraph security_features ["Security Features"]

SECURITY -->|Data Protection| ENCRYPTION

SECURITY -->|Data Integrity| ERROR_DETECTION

SECURITY -->|User Authentication| SIGN_AUTH

SECURITY -->|Data Correction| ERROR_CORRECTION

end

  

subgraph encryption_types ["Encryption Types"]

ENCRYPTION --> ASYMMETRIC --> RSA

ASYMMETRIC --> X25519

ENCRYPTION --> SYMMETRIC --> AES_GCM

SYMMETRIC --> CHACHA

end

  

subgraph error_detection_group ["Error Detection & Hashing"]

ERROR_DETECTION --> HASHING

ERROR_DETECTION --> CRC

HASHING --> ARGON_BCRYPT

HASHING --> SHA

end

  

subgraph signing_and_authentication ["Signing & Authentication"]

SIGN_AUTH --> RSA

SIGN_AUTH --> ED25519

SIGN_AUTH --> X509_CERT

end
````

**Good References**

1. [Practical Cryptography for Developers](https://cryptobook.nakov.com/)
