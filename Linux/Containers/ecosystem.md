---
aliases: []
author: Maneesh Sutar
date: 2024-05-03
tags:
- todo
- tofix
- public
- linux
- container
title: The Linux Container Ecosystem
---

# The Linux Container Ecosystem

## Organisations

[Organisations](Organisations.md)

Note: #todo  create combined diagram showing docker, podman, k8s, CRI, runtime env

## Colima

[colima](colima.md)

## k3d

[k3d](k3d.md)

## Podman

[podman](podman.md)

## CRI-O

[cri-o](cri-o.md)

## Docker

[Docker](Docker.md)

## Kubernetes

[Kubernetes](Kubernetes.md)

## tools

nerdctl: a cli for containerd (remember to use namspaces)  
crictl: a cli for CRI  
ctr: a non-supported cli for containerd

k3s: a cli for managing installed k3s cluster. Internally provides other commands like kubectl, crictl etc.

To get the logs (stdout) of a systemctl service:  
`sudo journalctl -u <service name> | less`
