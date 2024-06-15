---
aliases: []
author: Maneesh Sutar
date: 2024-01-05
tags:
- public
- linux
title: Inode
---

# Inode

[inode(7)](https://man7.org/linux/man-pages/man7/inode.7.html)

Each file has an inode containing metadata about the file.  An application can retrieve this metadata using [stat(2)](https://man7.org/linux/man-pages/man2/stat.2.html) (or related calls)

## Allocation of inodes

When disk is formatted with filesystem (usually ext4 for linux), an inode ratio is defined. By default the ratio is 1 inode per 16 KB, and the value 16KB can be changed during creation of filesystem

For every new file, an inode is used. If file size exceeds 16 KB, then another inode is created ==which is linked to previous inode==. In this way, for every increment of 16 KB, new inode is used.

It may happen that due to large number of very small files, the filesystem will run out of inodes. In such cases, we have to reformat the filesystem, may lead to data loss.

To see inode info of a file, run `stat <file>`

## Information in inode

==An inode does not contain the name of the file==

* Device where inode resides
* Inode number
* File type and mode: See [linux_file_types_and_modes](linux_file_types_and_modes.md)
* Link count: the number of hard [links](links.md)  to the file. 
* User ID: records the user ID of the owner of the file.
* Group ID: Records the ID of the group owner of the file.
* Device type: If this file (inode) represents a device, then the inode records the ==major and minor ID of that device==. Used for block and character special files , which are typically located in `/dev`. More on this [devices](devices.md)
* File size: file size in bytes. Length of the path string in case of [symbolic link](links.md)
* Preferred block size for I/O: This field indicates the number of blocks allocated to the file, 512-byte units, (This may be smaller than
* Number of blocks allocated to the file: This field indicates the number of blocks allocated to the file, 512-byte units,
* File creation (birth) timestamp (btime)
* Last access timestamp (atime):  
  It is changed by file accesses, e.g. execution, reading by any means. Also modified using `touch` commmand
* Last modification timestamp (mtime)  
  It is changed by file modification, e.g. writing, trucation. Also modified using `touch` commmand. It is *not* changed for changes in owner, group, hard link count, or mode.
* Last status change timestamp (ctime):   
  It is changed by modifications in *inode information* (i.e., owner, group, link count, mode, etc.).
