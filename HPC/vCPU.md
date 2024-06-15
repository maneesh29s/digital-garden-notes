---
aliases: []
author: Maneesh Sutar
date: 2023-06-16
tags:
- public
title: vCPU
---

# vCPU

## Pre-requisites

### Hypervisor

* software used to create and run virtual machines (VMs)
* allows one host computer to support multiple guest VMs by **virtually sharing its resources**

### Socket

* **array of pins** that hold a processor in place and connect the motherboard to the available processing power.

### Thread

* "a lightweight process"
* a path of execution **within a process**.
* Threads within same process run in shared memory space
* As an example, having multiple tabs open in a browser represents different threads.

### Physical core

* an independent single processing unit present on the CPU chip

### Logical core

* A logical core makes it possible for a **single physical core to perform two or more actions** simultaneously
* Logical cores made the concept of [Hyper-threading Technology](../ComputerArchitecture/intel_x86_64_architecture.md) possible, CPU can work on 2 tasks simultaneously
* There are limitations to hyper-threading versus the physical capabilities of the core.

## How does vCPU work?

vCPU represents **a portion or share of the underlying, physical CPU** that is assigned to a particular virtual machine (VM).

* Concept behind vCPUs : share of the time spent on the processor’s core
* Resource allocation is controlled by Hypervisor

## Calculations of available vCPU

$$(Threads\ \*\\ Cores)\ * Physical\_CPU = Number\_of\_vCPU$$

e.g. **Intel Xeon E-2288G** chipset has  8 cores / 16 threads  
Assuming we have 1 chipset in the motherboard  
Thus,  
$( 16 * 8 ) * 1 = 128\ vCPU$  
You can decide how many $vCPU$ s you want to allocate per Virtual Machine.  
Depending on the workload, you may get more or less VMs from the same compute. For example:  
**4 vCPUs per VM**  
128 vCPUs/4 vCPUs per VM = **32 VMs**

**2 vCPUs per VM**  
128 vCPUs/2 vCPUs per VM = **64 VMs**

# References

<https://www.datacenters.com/news/what-is-a-vcpu-and-how-do-you-calculate-vcpu-to-cpu>
