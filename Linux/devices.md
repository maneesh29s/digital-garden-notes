---
aliases: []
author: Maneesh Sutar
created: 2024-01-05
modified: 2024-09-28
tags:
- linux
title: Devices
---

# Devices in Linux

## Types of devices

### Character vs. block devices

 > 
 > from [tldp/devices](https://tldp.org/LDP/khg/HyperNews/get/devices/basics.html)

There are two main types of devices under all Unix systems, character and block devices. Character devices are those for which no buffering is performed, and block devices are those which are accessed through a cache. Block devices must be random access, but character devices are not required to be, though some are. Filesystems can only be mounted if they are on block devices.

Character devices are read from and written to with two function: foo_read() and foo_write(). The read() and write() calls do not return until the operation is complete. By contrast, block devices do not even implement the read() and write() functions, and instead have a function which has historically been called the "strategy routine".

Reads and writes are done through the buffer cache mechanism by the generic functions bread(), breada(), and bwrite(). These functions go through the buffer cache, and so may or may not actually call the strategy routine, depending on whether or not the block requested is in the buffer cache (for reads) or on whether or not the buffer cache is full (for writes). A request may be asyncronous: breada() can request the strategy routine to schedule reads that have not been asked for, and to do it asyncronously, in the background, in the hopes that they will be needed later.

The sources for character devices are kept in drivers/char/, and the sources for block devices are kept in drivers/block/. They have similar interfaces, and are very much alike, except for reading and writing. Because of the difference in reading and writing, initialization is different, as block devices have to register a strategy routine, which is registered in a different way than the foo_read() and foo_write() routines of a character device driver. Specifics are dealt with in [Character Device Initialization](https://tldp.org/LDP/khg/HyperNews/get/devices/char.html#init) and [Block Device Initialization](https://tldp.org/LDP/khg/HyperNews/get/devices/block.html#init).

We can use [mknod(1)](https://man7.org/linux/man-pages/man1/mknod.1.html) command to create a character or block file

## Device Driver

A program which help applications talk to hardware devices

### Major Minor numbers

<https://www.ibm.com/docs/en/linux-on-systems?topic=hdaa-names-nodes-numbers>

 > 
 > All devices controlled by the same device driver are given the same **major number**, and of those with the same major number, different devices are distinguished by different **minor numbers**.

When you run `stat` on a char/block device file, you will get 2 additional numbers, as **Device type**, in the format `major:minor`

The ==major number identifies the driver associated with the device==. The kernel uses the major number at open time to dispatch execution to the appropriate driver.

The ==minor number is used only by the driver== specified by the major number. The minor number ==provides a way for the driver to differentiate among different devices it controls==.

## Reference

1. A set of (old) articles which explain in detail how to create a linux driver: <https://tldp.org/LDP/khg/HyperNews/get/devices/devices.html>
1. Linux Device Drivers Books: https://www.xml.com/ldd/chapter/book/index.html
