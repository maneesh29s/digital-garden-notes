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

A[Protect your data] -->|Data Reversibility| B["<a class='internal-link is-unresolved' href='./encryption'>Encryption</a>"]

A -->|Data Integrity| C["<a class='internal-link is-unresolved' href='./hashing'>Hashing</a>"]

A -->|Authentication| D["<a class='internal-link is-unresolved' href='./signing'>Signing</a>"] --> E

A -->|Data correction| HC["<a class='internal-link is-unresolved' href='./error_correction'>Hamming Codes</a>"]

B --> E["<a class='internal-link is-unresolved' href='./rsa'>RSA</a>"]

B --> F["<a class='internal-link is-unresolved' href='./dh'>ECDH</a>"]

C --> G{Security?}

G -->|Highest| H[Argon2/Bcrypt]

G -->|Medium| I["<a class='internal-link is-unresolved' href='./sha'>SHA</a>"]

G -->|Low| J["<a class='internal-link is-unresolved' href='./crc'>CRC</a>"]


````
