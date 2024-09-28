---
aliases: []
author: Maneesh Sutar
date: 2024-09-01
tags: []
title: DHCP protocol
---

# DHCP protocol

Using **Dynamic Host Control Protocol** , a **DHCP Server** typically hosted on one of the router in your network, assigns IP addresses to the clients who ask for it.

**DHCP** is a UDP based protocol. The ==server== listens on UDP ==port 67==, and the ==client== listens on UDP port ==68==.

## Handshake

````txt
Client                  Server
------- DISCOVER --------->
<------- OFFER -----------
------- REQUEST ---------->
<----- ACKNOWLEDGE ------->
````

During DHCP handshake, the client and server exchange following information crucial for connectivity:

1. client's ip address with subnet mask
1. client's hostname
1. **The network's DNS server ip** (if exists, almost always on the router)
1. **The domain name** e.g. ".local". Used for DNS resolution of the hostnames in local network. e.g. "mypc.local"

Once **DHCP Server** assigns an IP address to a client, it also takes care of updating the corresponding **DNS server's** entry, adding a new entry containing the ==client's hostname and client's IP==.  
The local network's **DNS server** is also running on your router (typically) on ==port 53.==

## References

1. <https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol>
1. [Youtube: DHCP+DNS in Wireshark](https://youtu.be/FYcO4ZshG8Q)
