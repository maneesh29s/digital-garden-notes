---
aliases:
- TLS
- Transport Layer Security
author: Maneesh Sutar
created: 2024-07-06
modified: 2025-04-13
tags: []
title: Transport Layer Security
---

# Transport Layer Security

## TLS 1.2

Main reference: [RFC5246](https://datatracker.ietf.org/doc/html/rfc5246)

Also see [TLS Cypher Suites](cypher_suite.md) for more information on standard algorithms used in TLS for various cryptographic purposes ([hashing](hashing.md), [encryption](encryption.md), [signing](signature_authentication.md))

The overall flow of **TLS 1.2 Handshake** is given below:

````txt
  Client                                          Server

      ClientHello                  -------->
                                                      ServerHello
                                                     Certificate*
                                               ServerKeyExchange*
                                              CertificateRequest*
                                   <--------      ServerHelloDone
      Certificate*
      ClientKeyExchange
      CertificateVerify*
      [ChangeCipherSpec]
      {Finished}                   -------->
                                               [ChangeCipherSpec]
                                   <--------           {Finished}
      {Application Data}           <------->   {Application Data}

             Figure 1.  Message flow for a full handshake
       
 * Indicates optional or situation-dependent messages that are not
 always sent.

 {} Indicates messages protected using the master key derived after
 a successful handshake
 
   Note: To help avoid pipeline stalls, ChangeCipherSpec is an
   independent TLS protocol content type, and is not actually a TLS
   handshake message.
````

[Reference](https://datatracker.ietf.org/doc/html/rfc5246#autoid-32) slightly modified

### Hello messages

ClientHello and ServerHello contain a 28-byte long `random`  (generated using PRNG) which adds randomness to each handshake. This random is later used in

1. Deriving digital signature using server's private key corresponding to public key in the certificate
1. Deriving the master key
1. Finished message

### Server side

Server shares its [x_509](x_509.md) certificate which contains a public key and metadata about the server (website name, org name etc). Since a certificate is signed using the [Public Key Infrastructure](pki.md), client can be sure that the public key really belongs to the server that it is connecting to.

In case of [ephemeral diffie-hellman](dh.md#Types-of-keys) (DHE or ECDHE) `KeyExchangeAlgorithm`, server needs to send its temporary DH params or `ServerDHParams`. This is done using `ServerKeyExchange` message.  
The structure of `ServerKeyExchange` is as follow:

````cpp
struct {
   select (KeyExchangeAlgorithm) {
    // anonymous key exchange, no auhentication from any side
    case dh_anon:
    case ecdh_anon:
     ServerDHParams params;
    
    // ephemeral key-exchange algorithms
    case dhe_dss:
    case dhe_rsa:
    case ecdhe_rsa:
    case ecdhe_ecdsa:
     ServerDHParams params;
     digitally-signed struct {
      opaque client_random[32];
      opaque server_random[32];
      ServerDHParams params;
     } signed_params;
    
    // static key-exchange algorithms
    case rsa:
    case dh_dss:
    case dh_rsa:
    case ecdh_rsa:
    case ecdh_ecdsa:
     struct {} ; /* message is omitted */
   };
  } ServerKeyExchange;
````

[Reference](https://datatracker.ietf.org/doc/html/rfc5246#section-7.3) slightly modified based on [TLSECC](https://datatracker.ietf.org/doc/html/rfc4492#section-2)

To prevent [MITM](mitm.md) attacks, a **digital signature**  `signed_params` is sent in the `ServerKeyExchange` message. In `signed_params`, the 2 `random`s sent in Hello messages along with server's DH params are [signed](signature_authentication.md) using the **private key** ==corresponding to the== **public key** present in the server's certificate.  
The `signed_params` signature is omitted when performing an Anonymous TLS connection.

The entire `ServerKeyExchange` message is omitted when `KeyExchangeAlgorithm` ==is static== in nature i.e. uses long stored public-private keys, since (ideally) only the server has access to the "private key" / "private params" corresponding to "public key" / "public params" in the certificate. Without the private key, [MITM](mitm.md) attacks are difficult.

Typically in TLS only server authentication takes place. If server also wants client to authenticate itself (given that client holds a [x_509](x_509.md) certificate of its own), the server can send `CertificateRequest` message.

Finally, `ServerHelloDone` message is sent to denote end of server side messages.

### Client side

If server sends `CertificateRequest`, client sends its own [x_509](x_509.md) certificate to the server.  
If the client sends a certificate containing a [static diffie-hellman](dh.md#Types-of-keys) exponent (i.e., it is doing **fixed_dh client authentication**), then both client and server generate ==the same pre-master secret at every handshake.== ([refer](https://datatracker.ietf.org/doc/html/rfc5246#appendix-F.1.1.3)). This is fast, but really not recommended as we completely lose [Forward Secrecy](forward_secracy.md). In fixed_dh, `ClientKeyExchange` message is empty and `CertificateVerify` message is not sent.  
If the client sends a certificate containing [RSA](rsa.md) public key, then client uses the corresponding RSA private key to sign the `CertificateVerify` message.

If the agreed upon `KeyExchangeAlgorithm` is `RSA`, then client ==generates a random 46-byte== **PreMasterSecret**, and ==encrypts it using server's RSA public key== present in the server's certificate ([refer](https://datatracker.ietf.org/doc/html/rfc5246#section-7.4.7.1)). The `ClientKeyExchange` message contains this RSA `EncryptedPreMasterSecret`.

If the agreed upon `KeyExchangeAlgorithm` is one of the ["Diffie-Hellman"s](dh.md) (excluding fixed_dh), then `ClientKeyExchange` contains the client side public parameters of the diffie-hellman. ([refer](https://datatracker.ietf.org/doc/html/rfc5246#section-7.4.7.2))

The `CertificateVerify` is sent to provide explicit verification of a client certificate (if it is sent in the first place). It contains a **digital signature** over ==all the handshake messages sent till now (including this message)==. The digital signature is [signed](signature_authentication.md) using the private key corresponding to the public key present in the client certificate.

### Derivation of master key

[Reference](https://datatracker.ietf.org/doc/html/rfc5246#section-8.1)

The `pre_master_secret` is either

1. A PRNG generated by client in case of [RSA](rsa.md) key exchange mode
1. The shared secret generated after (any of the) [Diffie-Hellman](dh.md) key exchanges

For all key exchange methods, the same algorithm is used to convert  
the pre_master_secret into the master_secret.

````js
master_secret = PRF(pre_master_secret, "master secret",
    ClientHello.random + ServerHello.random)[0..47];
````

The `master_secret` is always ==exactly 48 bytes in length.==

The **psuedorandom function (PRF)** is defined [here](https://datatracker.ietf.org/doc/html/rfc5246#section-5)

### Start of encryption

The encryption starts only after `ChangeCipherSpec` is called. Till then none of the data is encrypted by any means.

The `Finished` is the first message that is encrypted using the decided [encryption](encryption.md) algorithm and the `master_secret`

The structure of finished message is like this ([refer](https://datatracker.ietf.org/doc/html/rfc5246#section-7.4.9))

````cpp
struct {
   opaque verify_data[verify_data_length];
} Finished;
      
verify_data
 PRF(master_secret, finished_label, Hash(handshake_messages))
 [0..verify_data_length-1];

finished_label
 For Finished messages sent by the client, the string
 "client finished".  For Finished messages sent by the server,
 the string "server finished".
````

Since `Finished` message's input contains an hash over the entire handshake messages, this guarantees that the handshake messages seen by both client and server are exactly same.

After Finished messages, both client and server can talk to each other using encrypted medium.

## TLS 1.3

Main reference: [RFC8446](https://datatracker.ietf.org/doc/html/rfc8446)

The **TLS 1.3 Handshake** is given below:

````txt
       Client                                           Server

Key  ^ ClientHello
Exch | + key_share*
     | + signature_algorithms*
     | + psk_key_exchange_modes*
     v + pre_shared_key*       -------->
                                                  ServerHello  ^ Key
                                                 + key_share*  | Exch
                                            + pre_shared_key*  v
                                        {EncryptedExtensions}  ^  Server
                                        {CertificateRequest*}  v  Params
                                               {Certificate*}  ^
                                         {CertificateVerify*}  | Auth
                                                   {Finished}  v
                               <--------  [Application Data*]
     ^ {Certificate*}
Auth | {CertificateVerify*}
     v {Finished}              -------->
       [Application Data]      <------->  [Application Data]

              +  Indicates noteworthy extensions sent in the
                 previously noted message.

              *  Indicates optional or situation-dependent
                 messages/extensions that are not always sent.

              {} Indicates messages protected using keys
                 derived from a [sender]_handshake_traffic_secret.

              [] Indicates messages protected using keys
                 derived from [sender]_application_traffic_secret_N.
````

[Reference](https://datatracker.ietf.org/doc/html/rfc8446#section-2)

Above diagram pretty much summarises everything we need to know about how handshake takes place.

TLS 1.3 heavily relies on [Extensions](https://datatracker.ietf.org/doc/html/rfc8446#section-4.2), as they are present in ClientHello, ServerHello and other messages.

Since client sends either a [key_share](https://datatracker.ietf.org/doc/html/rfc8446#section-4.2.8) or [pre_shared_key](https://datatracker.ietf.org/doc/html/rfc8446#section-4.2.11) (or both) along with the **ClientHello** message (1st message), ==server has all the data necessary to generate shared secrets and start encrypting its messages==. Once server sends its `key_share` or `pre_shared_key` , client has all the data to generated shared secrets.  
Thus ==TLS 1.3 is done within 1 round-trip== (1-RTT) instead of 2-RTT in TLS 1.2

TLS 1.3 added an improved [Pre-shared Key (PSK)](https://datatracker.ietf.org/doc/html/rfc8446#section-2.2) mechanism, which can be used for session resumptions. Addition of PSK also enables a [zero-RTT](https://datatracker.ietf.org/doc/html/rfc8446#section-2.3) mode.

TLS 1.3 has ==removed static RSA and static DH based key-exchange== mechanisms (see [Support in TLS](cypher_suite.md#Support-in-TLS)). All handshakes provide [Forward Secrecy](forward_secracy.md). All key exchanges (except when using **PSK**) take place using **Ephemeral Finite/Elliptical Diffie-Hellman**.

In Ephemeral key-exchanges cases, server must [authenticate](https://datatracker.ietf.org/doc/html/rfc8446#section-4.4) itself using [Certificate](https://datatracker.ietf.org/doc/html/rfc8446#section-4.4.2) and [CertificateVerify](https://datatracker.ietf.org/doc/html/rfc8446#section-4.4.3) messages.  
The `Certificate` message contains servers [x_509](x_509.md) certificate, which contains the public key using one of the [Digital Signature Algorithm](https://datatracker.ietf.org/doc/html/rfc8446#section-4.2.3) like [RSA](rsa.md) or [ECDSA](elliptical_curve_crypto.md#ECDSA)  
The `CertificateVerify` message ==contains a signature, over the== [hash of entire handshake message](https://datatracker.ietf.org/doc/html/rfc8446#section-4.4.1) upto that point, generated ==using the private key corresponding to the public key in the certificate..==

Unlike TLS 1.2, the ==handshake messages after server key exchange are encrypted== with keys derived from ==a set of 11 secrets==. Refer to [section 7.1](https://datatracker.ietf.org/doc/html/rfc8446#section-7.1) to see list of all the secrets (with how they are derived) and also [section 7.3](https://datatracker.ietf.org/doc/html/rfc8446#section-7.3) to see how the *key* and *iv* (required for [AES](aes.md) or [ChaCha20](chacha.md)) are derived from those secrets.

All key derivation processes use new [HKDF](hashing.md#HKDF) over the existing **PRF**.
