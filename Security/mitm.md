---
aliases:
- Man In The Middle
- MITM
author: Maneesh Sutar
created: 2024-05-31
modified: 2024-09-28
tags: []
title: Man In The Middle
---

# Man In The Middle

Wiki: <https://en.wikipedia.org/wiki/Man-in-the-middle_attack>

Attacker secretly relays and possibly alters the [communications](https://en.wikipedia.org/wiki/Data_communication "Data communication") between two parties who believe that they are directly communicating with each other, as the attacker has inserted themselves between the two parties

Even when using [RSA](rsa.md) or [ECDSA](dh.md#ECDSA) as user authentication algorithm, ==the MITM can actually impersonate both client and server using different public-private keys==. Thus middleman decrypt all the traffic going between client and server. (see this video on [key-exchange problem](https://youtu.be/vsXMMT2CqqE))  
Read the [signature and authentication](signature_authentication.md) to see how MITM impersonation is avoided.  
If an [MITM](mitm.md) can not impersonate client/server, its difficult for the middleman to decrypt the messages.

But, the ==middleman can alter the bits== of the message. To avoid this, **Message Authentication Codes** like [HMAC](hashing.md#HMAC) or [AEAD](aes.md#AES-GCM) are sent along with the message which determine the integrity of the message, thus [detecting any errors](error_detection.md).

In any case, the middleman can always ==hinder the communication== between 2 parties, such that none of the messages is ever validated due to errors.
