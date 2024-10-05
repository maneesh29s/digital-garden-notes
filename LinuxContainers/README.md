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


%% OCI-related flow

subgraph oci_flow ["OCI-related Flow"]

OCIRNTM["<a class='internal-link' href='./oci_container_runtimes'>OCI Container Runtimes</a>"]
R[runc]
C[crun]
G[gVisor]
K[kata containers]

OCIRNTM --> R
OCIRNTM --> C
OCIRNTM --> G
OCIRNTM --> K

end

  

%% Containerd workflow

subgraph containerd_flow ["Containerd Flow"]

CNTRDSK[containerd.sock]

CNTRD["<a class='internal-link' href='./containerd'>containerd</a>"]

CNTRDCRI["<a class='internal-link' href='./containerd#cri'>CRI plugin</a> <br> of containerd"]

  

CNTRDCRI --> |talks to|CNTRDSK

CNTRDSK --> |talks to| CNTRD

CNTRD ---> |calls| OCIRNTM

end

  

%% Main Docker Engine flow

subgraph docker_flow ["<a class='internal-link' align='left' href='./docker'>Docker</a> Flow"]

DCLI["<a href='https://docs.docker.com/reference/cli/docker/'>docker cli</a>"]

DSK[docker.sock]

DCRD["<a href='https://docs.docker.com/reference/cli/dockerd/'>Docker Engine(dockerd)</a>"]

  

DCLI --> |using| DSK

DSK --> |talks to| DCRD

DCRD --> |via| CNTRDSK

end

  
  

%% Subgraph for MacOS to Colima and Lima

subgraph mac_setup ["MacOS Setup"]

direction TB

MAC[MacOS]

COLIMA["<a class='internal-link' href='./colima'>Colima</a>"]

LIMA["<a class='internal-link' href='./lima'>Lima</a>"]

LVM[Linux VM]

MAC --> |"starts"| COLIMA

COLIMA --> |"starts"| LIMA

LIMA --> |"runs"| LVM

LVM --> |"exposes docker socket to"| MAC

LVM ---> |"runs"| DCRD

end

  
  

%% CRI-related workflow

subgraph cri_flow ["<a class='internal-link' href='./cri'>CRI</a> Flow"]

KBLT[kubelet]

CRIDSK[cri-docker.sock]

CRID["<a class='internal-link' href='./docker#cri-docker'>cri-docker</a>"]

CRIOSK[crio.sock]

CRIO["<a class='internal-link' href='./cri-o'>CRI-O</a>"]


KBLT --> |via| CNTRDCRI

KBLT --> |via| CRIDSK

CRIDSK ---> |talks to| CRID

CRID ---> |via| DSK

KBLT --> |via| CRIOSK

CRIOSK --> |talks to| CRIO

CRIO --> |calls| OCIRNTM

end

  

%% podman

subgraph podman ["Podman"]

PDMN["<a class='internal-link' href='./podman'>podman</a>"]

PDMN ---> |calls| OCIRNTM

end
````
