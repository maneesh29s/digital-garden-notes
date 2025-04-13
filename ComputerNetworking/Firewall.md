---
aliases: []
author: Maneesh Sutar
created: 2024-08-21
modified: 2025-04-14
tags: []
title: Firewall
---

# Firewall

A **firewall** is a network security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules.

There are many good online resources.  
This note contains answers to the some of the questions that I had regarding firewall.

## If firewall generally blocks all the ports, how are applications able to talk to internet?

* **Port Assignment:** When your application (Application A) makes a request to `google.com`, your operating system assigns an ephemeral port, say `54321`, for the outgoing connection. This port is used as the source port for this particular connection.
* Firewall typically ==allows all outbound connections== by default i.e. connections initiated by your application acting as a "client".
* The port `54321` is not globally open to the internet just because your application is using it. The ==firewall only permits inbound traffic that matches the connection initiated by your application==. Other unsolicited traffic trying to connect to port `54321`  will be blocked by the firewall.
* The firewall continues to protect the port from unauthorized access.
* Once the application closes, the port is released, and it no longer accepts any traffic until it is reassigned by the OS to another application or connection.

## What exactly happens when you open a port?

1. You are telling firewall to ==allow incoming traffic via that port from the public network== that your machine is connected to. This must be done if your machine is a "server" running applications like a web server (**nginx**) or ssh daemon (**sshd**).
1. The ==server will only handle the data== if
1. there is a service actively listening on that port
1. the service is capable of processing the incoming data according to the relevant protocol.
1. ==Ports that do not have a corresponding service will not handle incoming data== and will effectively ignore it.

## What exactly is Forwarding a port?

Using tools like `ssh` you can also forward your local ports to the remote ports.

Say you forward `localhost:8080` to the server (where `sshd` is running) port `8989`.

Then, the `ssh` client running on your machine, will forward the requests made to your `localhost:8080` to the server's port `8989` .

If an application is running on the server, actively listening to port `8989` , it will process the incoming data and respond back to it using the same port `8989`. Again, that responce will be sent back to your `localhost:8080` by `sshd` .

## References

1. [Wiki](https://en.wikipedia.org/wiki/Firewall_(computing))
