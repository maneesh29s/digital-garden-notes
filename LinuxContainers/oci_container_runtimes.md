---
aliases: []
author: Maneesh Sutar
date: 2024-05-11
tags:
- linux/container
title: OCI Container Runtimes
---

# OCI Container Runtimes

All these container runtime conform to the [OCI runtime Spec](https://github.com/opencontainers/runtime-spec)

This page mentions how these runtimes are integrated with [containerd](containerd.md) specifically, although other tools like [podman](podman.md) and [cri-o](cri-o.md) can also use any of these runtimes.  
You can read the [containerd](containerd.md) page to know details about containerd's shim + runtime engine architecture.

## runc

<https://github.com/opencontainers/runc>  
First donated by docker to OCI.  
runc became the reference implementaion for developing the OCI runtime spec.  
Default in docker and containerd

`containerd` uses the default `containerd-shim-runc-v2` "runtime shim" to invoke the `runc`.  
The `runc` is the "runtime engine".

## crun

<https://github.com/containers/crun>  
developed under "containers" organisation (same as podman) by RedHat  
written in C  
I am not sure if a containerd shim binary is available to be used with crun.

## kata-runtime

<https://github.com/kata-containers/kata-containers>  
For **Hypervisor** (VM) based containers  
They support many [Hypervisors](https://github.com/kata-containers/kata-containers/blob/main/docs/hypervisors.md) such as Firecracker, QEMU, Cloud Hypervisor.

Earlier [runv (EOL)](https://github.com/hyperhq/runv) , now [kata-runtime](https://github.com/kata-containers/kata-containers/tree/main/src/runtime/README.md) which is part of the same kata-containers project  
See [software details](https://katacontainers.io/software/) and [architecture](https://github.com/kata-containers/kata-containers/tree/main/docs/design/architecture) for more details

The kata-runtime is [OCI](https://github.com/opencontainers/runtime-spec)-compatible, [CRI-O](https://github.com/cri-o/cri-o)-compatible, and [Containerd](https://github.com/containerd/containerd)-compatible, allowing it to work seamlessly with both Docker and Kubernetes respectively.

Kata Containers 1.5 introduced the `shimv2` for containerd 1.2.0, [reducing the components required](https://github.com/kata-containers/kata-containers/blob/main/docs/design/architecture/history.md)  to spawn pods and containers (from `2N + 1` shims to `1` shim per Pod).  
Now `containerd`  can invoke kata-runtime containers using the `containerd-shim-kata-v2` runtime shim.  
**Hypervisor** acts as the runtime engine.

As of Kata Containers v3.4.0,  
The `CRI-O + Kata` [setup for k8s](https://github.com/kata-containers/kata-containers/blob/main/docs/how-to/run-kata-with-k8s.md#cri-o) also uses `containerd-shim-kata-v2` as [runtime path](https://github.com/cri-o/cri-o/blob/main/docs/crio.conf.5.md#crioruntimeruntimes-table) while specifying the [runtime type](https://github.com/cri-o/cri-o/blob/main/docs/crio.conf.5.md#crioruntimeruntimes-table) as "vm".  
An **equivalent shim implementation** for CRI-O is [planned](https://github.com/kata-containers/kata-containers/blob/main/docs/how-to/run-kata-with-k8s.md#install-a-cri-implementation).

## gVisor

<https://github.com/google/gvisor>  
Provides more isolated environment for containers, than the default shared kernel containerisation  
Read [docs](https://gvisor.dev/docs/) to know how it is different than VM or SELinux

`containerd` can invoke gVisor based containers using `containerd-shim-runsc-v1` runtime shim.  
gVisor uses its own `runsc` runtime engine.  
<https://gvisor.dev/docs/user_guide/containerd/quick_start/>
