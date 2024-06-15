---
aliases: []
author: Maneesh Sutar
date: 2024-01-05
tags:
- todo
- tofix
- public
- linux
title: Devices
---

# Devices

<https://tldp.org/LDP/khg/HyperNews/get/devices/basics.html>

<https://www.ibm.com/docs/en/linux-on-systems?topic=hdaa-names-nodes-numbers>

We can use [mknod(1)](https://man7.org/linux/man-pages/man1/mknod.1.html) command to create a character or block file

## Character Devices

## Block Devices

## Major Minor numbers

When you run `stat` on a char/block device file, you will get 2 additional numbers, as **Device type**, in the format `major:minor`

The ==major number identifies the driver associated with the device==.  
The kernel uses the major number at open time to dispatch execution to the appropriate driver.

The ==minor number is used only by the driver== specified by the major number. The minor number ==provides a way for the driver to differentiate among different devices it controls==.
