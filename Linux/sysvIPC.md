---
aliases: []
author: Maneesh Sutar
created: 2024-01-05
modified: 2025-04-14
tags:
- linux
title: System V IPC
---

# System V IPC

System V IPC is the name given to three interprocess communication mechanisms that are widely available on UNIX systems: **message queues, semaphore, and shared memory**.

For System V IPC APIs visit [sysvipc(7)](https://man7.org/linux/man-pages/man7/sysvipc.7.html)

Although [POSIX](POSIX.md) ==provides alternative APIs for each mechanism==, the functionality is same in both SysV and POSIX APIs.

## Message queues

System V message queues allow data to be ==exchanged in units called messages==. Each message can have an associated priority.  
See POSIX message queue [mq_overview(7)](https://man7.org/linux/man-pages/man7/mq_overview.7.html)

## Semaphores

System V **semaphores** allow ==processes to synchronise their actions==. System V semaphores are allocated in groups called sets; each semaphore in a set is a ==counting semaphore==.

See POSIX semaphores [sem_overview(7)](https://man7.org/linux/man-pages/man7/sem_overview.7.html).

 > 
 > A semaphore is an integer whose value is never allowed to fall below zero.  Two operations can be performed on semaphores:  
 > increment the semaphore value by one ([sem_post(3)](https://man7.org/linux/man-pages/man3/sem_post.3.html)); and decrement the semaphore value by one ([sem_wait(3)](https://man7.org/linux/man-pages/man3/sem_wait.3.html)).  
 > If the value of a semaphore is currently zero, then a [sem_wait(3)](https://man7.org/linux/man-pages/man3/sem_wait.3.html) operation will block until the value becomes greater than zero.

## Shared memory segments

System V shared memory allows processes to share a region a  memory (a "segment"). See POSIX shared memory [shm_overview(7)](https://man7.org/linux/man-pages/man7/shm_overview.7.html)
