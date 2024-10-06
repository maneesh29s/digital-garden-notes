---
aliases: []
author: Maneesh Sutar
created: 2023-12-30
modified: 2024-09-28
tags:
- linux
title: Linux Pipes
---

# Linux Pipes

ref: <https://man7.org/linux/man-pages/man7/pipe.7.html>

provide a unidirectional interprocess communication channel

A pipe is created using [pipe(2)](https://man7.org/linux/man-pages/man2/pipe.2.html) which creates a new pipe and returns two file descriptors, one referring to the read end of the pipe, the other referring to the write end.

There's also [FIFO_pipes](FIFO_pipes.md) , which are named pipes

A pipe has a limited capacity (default 16 pages, each page 4KiB), an application should be designed so that a reading process consumes data as soon as it is written by writing process.

Memory used for pipes can be configured by modifying the values present in `/proc/sys/fs/pipe-*` files
