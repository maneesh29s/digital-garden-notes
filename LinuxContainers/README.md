---
aliases: []
author: Maneesh Sutar
date: 2024-06-16
tags: []
title: Linux Container Ecosystem
---

# Folder: Linux Container Ecosystem

## Tools

````mermaid
flowchart TD

DCLI["<a href='https://docs.docker.com/reference/cli/docker/'>docker cli</a>"] --> |using| DSK[docker.sock] --> |talks to| DCRD["<a href='https://docs.docker.com/reference/cli/dockerd/'>Docker Engine(dockerd)</a>"]

KBLT[kubelet] --> |via| CRIDSK[cri-docker.sock] --> |talks to| CRID[""<a class='internal-link' href='./docker#cri-docker'>cri-docker</a>""] --> |via| DSK

DCRD -->|via| CNTRDSK[containerd.sock] --> |talks to| CNTRD["<a class='internal-link' href='./containerd'>containerd</a>"]

KBLT --> |"via <a class='internal-link' href='./containerd#CRI'>CRI plugin</a> <br> of containerd"| CNTRDSK

KBLT --> |via| CRIOSK[crio.sock] --> |talks to| CRIO["<a class='internal-link' href='./cri-o'>CRI-O</a>"] --> |calls| OCIRNTM

CNTRD --> |calls| OCIRNTM["<a class='internal-link' href='./oci_container_runtimes'>OCI Container Runtimes</a>"]

PDMN["<a class='internal-link' href='./podman'>podman</a>"] --> |calls| OCIRNTM

OCIRNTM --> R[runc] 

OCIRNTM --> C[crun]

OCIRNTM --> G[gVisor]

OCIRNTM --> K[kata containers]

````
