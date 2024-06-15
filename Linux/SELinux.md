---
aliases:
- SELinux
author: Maneesh Sutar
date: 2023-11-19
tags:
- public
- linux
title: Security Enhanced Linux
---

# Security Enhanced Linux

[Reference](https://www.redhat.com/en/topics/linux/what-is-selinux#overview)

Security-Enhanced Linux (SELinux) is a security architecture for linux systems that allows administrators to have more control over who can access the system.  
It was originally developed by the **United States National Security Agency (NSA)** as a series of patches to the Linux kernel using **Linux Security Modules (LSM**), then SELinux was merged into the [Linux kernel mainline](https://en.wikipedia.org/wiki/Linux_kernel_mainline "Linux kernel mainline") in the 2.6 series of the Linux kernel.

It defines access controls for the applications, processes, and files on a system.

When an application or process, known as a subject, makes a request to access an object, like a file, SELinux checks with an **access vector cache (AVC)**, where permissions are cached for subjects and objects.

If SELinux is unable to make a decision about access based on the cached permissions, it sends the request to **the security server**. The security server checks for the security context of the app or process and the file

## SELinux labeling and type enforcement

SELinux works as a **labeling system**, which means that all of the ==files, processes, and ports in a system have an SELinux label== associated with them.  
Labels are a logical way of grouping things together. The kernel manages the labels during boot.

**Labels format** ==user:role:type:level== (level is optional).  
User, role, and level are used in more advanced implementations of SELinux, like with MLS.  
Label type is the most important for targeted policy.

**Type enforcement** is the part of an SELinux policy that ==defines whether a process running with a certain type can access a file labeled== with a certain type.

## Enabling SELinux

Enable SElinux by editing `/etc/selinux/config` and  
There are 2 variables which can be configured:

1. **SELINUX** enables/disables SE linux  
   enforcing - SELinux security policy is enforced.  
   permissive - SELinux prints warnings instead of enforcing.  
   disabled - No SELinux policy is loaded.

1. **SELINUXTYPE**  
   targeted - Targeted processes are protected,  
   minimum - Modification of targeted policy. Only selected processes are protected.  
   mls - Multi Level Security protection.

We can also run command `setenforce 1` to enforce SELinux if it is disabled

Though, changing from disabled to enforcing is not recommended, as it can break the system (e.g. enable to boot) due to improper labels. Follow the guidelines in the documentation.

## Discretionary access control (DAC) vs. mandatory access control (MAC)

With DAC, files and processes have owners (user, group or others).  
Users have the ability to change permissions on their own files.  
The ==root user has full access control with a DAC== system.

But on MAC systems like SELinux, there is ==administratively set policy around access==.  
Even if the DAC settings on your home directory are changed, an ==SELinux policy in place to prevent another user or process from accessing the directory will keep the system safe==.  
SELinux policies let you be specific and cover a large number of processes. You can make changes with SELinux to limit access between users, files, directories, and more.

## What are booleans?

Booleans are ==on/off settings for functions in SELinux==.  
There are hundreds of settings that can turn SELinux capabilities on or off, and many are already predefined. You can find out which booleans have already been set in your system by running getsebool -a.
