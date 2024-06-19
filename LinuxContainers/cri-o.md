---
aliases: []
author: Maneesh Sutar
date: 2024-05-10
tags:
- public
- linux
- container
title: CRI-O
---

# CRI-O

CRI-O

its whole purpose is to be the CRI for container orchestrators like k8s  
So it can do what CRI should do, e.g. transfer of images, image storage, networking, container monitoring,  etc and NOTHING else like building images, or letting user start containers via CLI  
See <https://github.com/cri-o/cri-o?tab=readme-ov-file#what-is-the-scope-of-this-project> and out of scope

Like podman, CRI-O depends on other opensource libraries like image, storage, cni, conmon, and OCI runtimes like runc

CRI-O is developed by redhat, intel, ibm, suse and hyper

CRI-O can only PULL images, not PUSH  
because ImagerService in CRI spec <https://github.com/kubernetes/kubernetes/blob/release-1.5/docs/proposals/container-runtime-interface-v1.md#container-runtime-interface> only supports pull operation

Anyway CRI-O relies on external library container/images which is capable of pull/push
