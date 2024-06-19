---
aliases: []
author: Maneesh Sutar
date: 2024-06-16
tags:
- public
title: Linux Container Ecosystem
---

# Folder: Linux Container Ecosystem

## Tools

````mermaid
flowchart TD

DCLI["<a href='https://docs.docker.com/reference/cli/docker/'>docker cli</a>"] --> |using| DSK[docker.sock] --> |talks to| DCRD["<a href='https://docs.docker.com/reference/cli/dockerd/'>Docker Engine(dockerd)</a>"]

KBLT[kubelet] --> |via| CRIDSK[cri-docker.sock] --> |talks to| CRID[cri-docker] --> |via| DSK

DCRD -->|via| CNTRDSK[containerd.sock] --> |talks to| CNTRD["<a class='internal-link' href='./containerd'>containerd</a>"]

KBLT --> |"via <a class='internal-link' href='./Kubernetes#CRI'>CRI</a> plugin"| CNTRDSK

KBLT --> CRIO["<a class='internal-link' href='./cri-o'>CRI-O</a>"] --> PDMN["<a class='internal-link' href='./podman'>podman</a>"]

CNTRD --> |calls| OCIRNTM["<a class='internal-link' href='./oci_container_runtimes'>OCI Container Runtimes</a>"]

PDMN --> |calls| OCIRNTM

OCIRNTM --> R["<a href='https://github.com/opencontainers/runc'>runc</a>"] 

OCIRNTM --> C["<a href='https://github.com/containers/crun'>crun</a>"]

OCIRNTM --> G[gVisor]

OCIRNTM --> K[kata containers]

````
