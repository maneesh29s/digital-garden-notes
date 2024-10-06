---
aliases: []
author: Maneesh Sutar
created: 2023-12-30
modified: 2024-09-28
tags:
- linux
title: FIFO in linux
---

# FIFO in linux

Ref: <https://man7.org/linux/man-pages/man7/fifo.7.html>

A FIFO special file is like a [pipe](pipe.md), except that it is ==accessed as part of the filesystem.==  
Its kind of a ==named pipe==

the FIFO special file has no contents on the filesystem; the filesystem entry merely serves as a reference point so that processes can access the pipe using a name in the filesystem

[mkfifo(1)](https://man7.org/linux/man-pages/man1/mkfifo.1.html) command can create FIFO files.

[mkfifo(3)](https://man7.org/linux/man-pages/man3/mkfifo.3.html) is a standard C library function, and the recommended way to create an FIFO file. I think it calls [mknod(2)](https://man7.org/linux/man-pages/man2/mknod.2.html) syscall with appropriate optios to create FIFO files.
