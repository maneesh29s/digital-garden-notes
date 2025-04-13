---
aliases: []
author: Maneesh Sutar
created: 2024-01-05
modified: 2025-04-14
tags:
- linux
title: tmpfs
---

# tmpfs

[tmpfs(5)](https://man7.org/linux/man-pages/man5/tmpfs.5.html)

The **tmpfs** facility allows the creation of filesystems whose contents reside in virtual memory (RAM).  
Since the files on such ==filesystems typically reside in RAM, file access is extremely fast==.

If a **tmpfs** filesystem is unmounted, or machine is shut down, all its contents are discarded (lost).

A **tmpfs** filesystem has the following properties:

•  The filesystem can employ swap space when physical memory pressure demands it.

•  The filesystem ==consumes only as much physical memory and swap space as is required== to store the current contents of the filesystem. Even though, running `df -h` on a tmps volume will show its maximum size (by default) as 50% of the physical RAM

•  During a remount operation (*mount -o remount*), the filesystem size can be changed (without losing the existing contents of the filesystem).
