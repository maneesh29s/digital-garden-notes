---
aliases: []
author: Maneesh Sutar
date: 2023-12-18
tags:
- linux
title: Linux File Types and File Modes
---

# Linux File Types and File Modes

More info on [inode manpage](https://man7.org/linux/man-pages/man7/inode.7.html#:~:text=the-value-0.-,The-file-type-and-mode,-The-stat.st_mode)

File type and permission are stored as a **16-bit "value"**

**Higher 4-bits:** for storing file type (max 16 file type possible)

**Lower 12-bits:** for storing permissions : for special, user, group, other : each can have 7 combinations of read-write-execute + 1 for no permission

The "value" is typically represented in octal notation.

e.g. A regular file with rwxr--r-- permission will have value "0100744", where  
0 - no idea why its there  
10 - regular file  
0744 - file permissions

## File types

Each file can have ==only 1 file type==

( 'x' in the value column corresponds to file mode )

|Value (octal)|Notes|
|-------------|-----|
|014xxxx|socket|
|012xxxx|symbolic link|
|010xxxx|regular file|
|006xxxx|block device|
|004xxxx|directory|
|002xxxx|character device|
|001xxxx|FIFO|

## File modes

Special permissions (set UID, set GID, sticky) have higher priority over other permissions  
You can combine the permissions by adding the values  
e.g. 4754: set UID enabled, u=rwx, g=rx, o=r

( 'x' in the value column corresponds to file mode )

|Value (octal)|Notes|
|-------------|-----|
|0xx4000|set UID bit|
|0xx2000|set-group-ID bit (see below)|
|0xx1000|sticky bit (see below)|
|0xx0400|owner has read permission|
|0xx0200|owner has write permission|
|0xx0100|owner has execute permission|
|0xx0040|group has read permission|
|0xx0020|group has write permission|
|0xx0010|group has execute permission|
|0xx0004|others have read permission|
|0xx0002|others have write permission|
|0xx0001|others have execute permission|
