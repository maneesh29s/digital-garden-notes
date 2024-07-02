---
aliases: []
author: Maneesh Sutar
date: 2024-05-31
tags:
- public
title: Security
---

# Folder: Security

**Purpose**

1. To protect data from getting in the hands on unauthenticated users
1. To preserve integrity of the data during transport

````mermaid
flowchart TD

A[Security] 
B["<a class='internal-link' href='./encryption'>Encryption</a>"]
C["<a class='internal-link ' href='./error_detection'>Error Detection</a>"]
D["<a class='internal-link' href='./signature_authentication'>Signing and Authentication</a>"]
E["<a class='internal-link' href='./rsa'>RSA</a>"]
F["<a class='internal-link' href='./dh#ECDH'>X25519</a>"]
H[Argon2/Bcrypt]
I["<a class='internal-link' href='./sha'>SHA</a>"]
J["<a class='internal-link' href='./crc'>CRC</a>"]
L["<a class='internal-link' href='./dh#ECDSA'>ed25519</a>"]
HC["<a class='internal-link' href='./error_correction'>Error Correction</a>"]

SYM[Symmetric]
ASYM[Asymetric]
AES["<a class='internal-link' href='./aes'>AES-GCM</a>"]
CHA["<a class='internal-link' href='./chacha'>ChaCha20-Poly1305</a>"]
HASH["<a class='internal-link' href='./hashing'>Hash</a>"]

A -->|Data Protection| B

A -->|Data Integrity| C

A -->|User Authentication| D 
D --> E
D --> L

A -->|Data correction| HC

B --> ASYM --> E
ASYM --> F
B --> SYM --> AES
SYM --> CHA

C --> HASH
C --> J
HASH --> H
HASH --> I

````
