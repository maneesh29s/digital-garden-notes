---
aliases: []
author: Maneesh Sutar
date: 2024-05-10
tags:
- public
- linux
- container
title: containerd
---

# containerd

Was a part of [docker](docker.md)

See [architecture](https://containerd.io/img/architecture.png)

**nerdctl**: a cli for containerd (remember to use namspaces)

## Shim runtime API

Refer: <https://github.com/containerd/containerd/tree/main/core/runtime/v2#architecture>  
The shim (runtime) v2 is introduced in containerd [v1.2.0](https://github.com/containerd/containerd/releases/tag/v1.2.0)

containerd support multiple OCI runtimes such as runc, kata, runsc (gVisor).  
As a common abstraction, containerd has provided the runtime API.

containerd, the daemon, **does not directly launch containers. Instead, it acts as a higher-level manager** or hub for coordinating the activities of containers and content, that lower-level programs, called "**runtimes**", actually implement to start, stop and manage containers.

Two common patterns for implementation of a runtime are:

* a **single binary for runtime** that both listens on the socket and creates/starts/stops the container
* "**shim+engine**": a separate **runtime shim** binary that listens on the socket, and invokes a separate **runtime engine** that creates/starts/stops the container

The "shim+engine" pattern is used because it makes it easier to integrate distinct runtimes implementing a specific runtime engine spec, such as the [OCI runtime spec](https://github.com/opencontainers/runtime-spec).  
The ttRPC protocol can be handled via one runtime shim, while distinct runtime engine implementations can be used, as long as they implement the OCI runtime spec.  
For example of this pattern,  [runc](https://github.com/opencontainers/runc), which implements the [OCI runtime spec](https://github.com/opencontainers/runtime-spec) is a runtime *engine*. Thus it is not invoked directly by `containerd`; instead, it is invoked by `containerd-shim-runc-v2` shim , which listens on the socket for requests from `containerd`.

Some common "runtimes":

1. [runc](https://github.com/containerd/containerd/tree/main/core/runtime/v2#invoking-runtimes) = Runtime option : `io.containerd.runc.v2`   Shim BInary: `containerd-shim-runc-v2` Shim Engine: [runc](https://github.com/opencontainers/runc)
1. [kata](https://github.com/kata-containers/kata-containers/blob/main/docs/design/architecture/example-command.md) = Runtime option : `io.containerd.kata.v2`   Shim BInary: `containerd-shim-kata-v2` Engine: HyperVisor
1. [gVisor](https://gvisor.dev/docs/user_guide/quick_start/docker/) = Runtime option: `io.containerd.runsc.v1`   Shim BInary:  `containerd-shim-runsc-v1` Engine: [runsc](https://gvisor.dev/docs/)

The runtime (typically `--runtime`) can be selected when creating a container via one of the exposed containerd services (containerd client, CRI API,...), or via a client that calls into the containerd provided services.  
The containerd clients are ( `ctr`, `nerdctl`, `kubernetes`, `dockerd`).

## cri

Also see: <https://kubernetes.io/blog/2018/05/24/kubernetes-containerd-integration-goes-ga/>

The [CRI](kubernetes.md#CRI) interface for kubelets to work with containerd directly

![containerd_cri](Artifacts/containerd_cri.png)

Also, the docker installed containerd (package `containerd.io`) disables the cri plugin  in containerd  (by modifying the /etc/containerd/config.toml config file ). Because cri plugin depends on cni (and maybe other libraries) which are not included when we install docker engine, so anyway the plugin won't run

You can tell containerd to run cri plugin by modifying the config file, but it will probably fail
