---
aliases:
- Lima
- Linux on Mac
author: Maneesh Sutar
created: 2024-10-05
modified: 2024-10-05
tags:
- linux
- vm
title: Lima
---

# Lima

[Lima](https://github.com/lima-vm/lima) or **Linux on Mac**

Can be used to run a linux virtual machine on mac.  
[Colima](colima.md) actually uses lima to first start a linux virtual machine, and then run docker inside it.

 > 
 > This article is a summary of my observations from various experiments I conducted with lima. It might be a little unstructured, so bare with me.

## VMTypes and their performance

Main article: <https://lima-vm.io/docs/config/vmtype>  
Lima supports 2 VMTypes: [QEMU](#qemu) and [VZ](#vz)

### QEMU

Repo: <https://gitlab.com/qemu-project/qemu>

The OG emulator, open source, cross platform.

Although QEMU can do a lot of emulations, in lima, its used mainly for 2 purposes:

1. **qemu-x86_64**: To emulate an x86_64 linux
1. **qemu-arch64**: To emulate an arch64 linux

 > 
 > If you run `htop` on host (mac), you will see the `qemu-system` process corresponding to the VM that you are running.

QEMU ==supports both userspace emulation and entire machine== (hardware) level emulation. But **I guess** ==Lima defaults to== the **machine level** emulation.

 > 
 > Refer to the diagram in the [this](https://lima-vm.io/docs/config/vmtype) article for summary of what to use when

From my experiments, running an ==x86_64 Ubuntu VM on on M1 Mac using QEMU was very slow==, which is also expected since this is cross-architecture run.  
Although I need to look for benchmarks comparing same-architecture performance of QEMU on Mac (intel vs M1).

### VZ

Repo: <https://github.com/Code-Hex/vz>

VZ is a **new and faster** emulator **specifically for Mac** because VZ uses  [Apple's native virtualization API](https://developer.apple.com/documentation/virtualization?language=objc) .

 > 
 > If you run `htop` on host (mac), you will see the `AppleVirtualizationFramework` process running corresponding to the VM.

VZ is **still experimental**. Lima falls back to [QEMU](#qemu) if VZ requirements are not met.

 > 
 > VZ will become the [default VMType](https://lima-vm.io/docs/config/vmtype/#vz) once lima reaches v1.0

But **I guess** based on [this diagram](https://lima-vm.io/docs/config/vmtype), VZ only does **userspace emulation**. The way it works is VZ requires a ==VM which is of same architecture as the host mac== ( #todo need to verify this ). So we can't specify a different architecture using `--arch` when `--vmtype vz` is passed. Then it translates the system calls on the VM to MacOS kernel calls.

==On M1 macs==, although the VM OS will always be aarch64 linux, one can enable [Rosetta 2](https://en.wikipedia.org/wiki/Rosetta_(software))   ==to run x86_64 containers inside aarch64 linux==. In lima this is done by passing `--vz-rosetta` option. The  ==containers can run in a different architecture== using docker's `--platform` option.

 > 
 > Can intel mac run aarch64 containers using VZ? #todo

### Benchmarks

Here is a benchmark on 2020 M1 Macbook Air, ran by Josh Byranes  
<https://github.com/ctrlok/macdockergeek/issues/3>
