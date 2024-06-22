---
aliases: []
author: Maneesh Sutar
date: 2024-05-10
tags:
- public
- linux
- container
title: podman
---

# podman

Podman does what docker and containerd can do i.e. manage images, containers

Docker is a complete networking storage image packaging solution on its own,  
containerd also has some own storage networking and image transfer solutions,  
podman relies on other open source libraries like image, storage, neavark etc. for its working  
See <https://github.com/containers/podman?tab=readme-ov-file#oci-projects-plans>

The main difference is, while docker and containerd follow a client-server (server being a daemon) model and use gRPC to communicate, podman uses traditional fork-exec model to start containers  
Since there is no daemon (system service) running all the time in background, podman runs "daemonless" and "rootless"

Other thing is docker has cri-docker, containerd has cri, but  CRI is not in the scope of podman. So podman can be used with container orchstrators like k8s.  
In such case, a dedicated CRI runtime like CRI-O can work with k8s.

See the [scope of podman](https://github.com/containers/podman?tab=readme-ov-file#overview-and-scope) and also what's out of scope in the same readme

docker engine (dockerd) provides lot of UX enhancing features like the cli, and extra features like image building (dockerfile), image transfers , high level network and storage,  etc.  
containerd works at a level lower than docker,  
docker relies on containerd for some things like container execution and supervision, low-level storage and network

but podman is a tool, which relies on other third party libraries (containers/image, containers/storage), and provides all of the commonly used features of docker and containerd combined. The "podman cli" takes inspiration from docker-cli, and can act as drop-in replacement (alias docker=podman)  
Podman internally uses "libpod" library. Also [visit this](https://github.com/containers/podman?tab=readme-ov-file#oci-projects-plans) for list of all the open source libraries it depends on.

## rootless podman behind the scenes

Note: #todo Read the reference  
Refer: <https://www.redhat.com/sysadmin/behind-scenes-podman?intcmp=7013a0000025wJwAAI>

### Namespaces in podman

Namespaces in podman: <https://youtu.be/Ac2boGEz2ww>

#### subuid

`/etc/subuid`: holds number of subordinate uids (subuids) that a user can create in its own namespace. This file contains list of all users and their subuids  
Typically its stored as:

`username/UID:starting subUID:range of subUID`

e.g.

````bash
1000:100000:65535
1500:200000:65535
````

#### uid_map

`/proc/$$/uid_map`: for a given process, this virtual file stores the UID mapping between current namespace and parent namespace  
This uid mapping depends on which user started the parent process (in our case the container) (among other things)  
Typically its stored as

`ID-inside-ns   ID-outside-ns   length`

e.g.  Following is present in `/proc/self/uid_map`, where `self` points to current process

````bash
0 1000 1
1 100000 65535
````

1st line indicates that,  
inside: namespace starts at UID 0 (root for the container)  
outside: namespace starts at UID 1000 (UID of the user who executed it)

So UID 0 in the container maps to UID 1000 outside the container

2nd line Indicates that,  
inside: namespace starts at UID 1  
outside: namespace starts at UID 100000  
So mapping is as follow: UID 1 => UID 100000 ; UID 4000 => UID 103999 and so on

## Relevent commands

### podman-unshare

[Docs](https://docs.podman.io/en/latest/markdown/podman-unshare.1.html)

==Launches a process== (command passed as argument OR by default *$SHELL*) in a ==new user namespace==.  
The user namespace is configured so that the ==invoker user’s UID and primary GID== appear to be UID 0 and GID 0, respectively. ==Any ranges which match that user and group in `/etc/subuid` and `/etc/subgid` are also mapped in as themselves== with the help of the *newuidmap(1)* and *newgidmap(1)* helpers  
e.g.  
Assuming the current user is 1000, and `/etc/subuid` has following records:

````bash
1000:100000:65535
````

Then, running following command

````bash
podman unshare
````

will execute `$SHELL` and create a new shell with the namespace of current user i.e. 1000  
The `/proc/self/uid_map` should look like:

````bash
0 1000 1 
1 100000 65535
````

So whatever commands you run in the new shell,  it will look like you are running them as the root (although you are actually running them as user 1000)

**podman unshare** is useful for troubleshooting unprivileged operations and for manually clearing storage and other data related to images and containers.
