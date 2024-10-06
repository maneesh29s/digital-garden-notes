---
aliases: []
author: Maneesh Sutar
created: 2024-05-10
modified: 2024-10-05
tags:
- linux/container
title: k3d.md
---

## k3d

<https://k3d.io/stable/>

k3d allows k3s to be run inside a docker container

By default, when run k3d create cluster my-cluster, it will create a docker container "k3d-my-cluster-server-0" which will act as one of the node of k3s. inside node, It will use a custom OS by k3s, install k3s components along with containerd, and run the k3s server with containerd socket /run/k3s/containerd/containerd.sock

As far as I see, k3d does not support creating a k3s cluster with --docker, so cri-docker or docker engine is not available with k3s cluster

k3d will use the embedded containerd (installed along with k3s) by default
