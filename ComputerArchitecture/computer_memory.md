---
aliases:
- RAM
- Memory
author: Maneesh Sutar
created: 2025-02-10
modified: 2025-02-10
tags:
- computer-architecture
title: Computer Memory
---

# Computer Memory

## How RAM works

**References:**

1. Animation video, focused on DDR5 features: [Link](https://youtu.be/7J7X7aZvMXQ).
1. Lecture by Onur Mutlu on Memory Organization: [Link](https://youtu.be/CDOOxhRBMIY?list=PL5Q2soXY2Zi-EImKxYYY1SZuGiOAOBKaf) . This Explains typical theory behind memory structure, which is valid across all generations of DDR ram.

## The Memory Specification

A PC RAM stick (the one we see typically in the market) can be specified using following sets of words:

`(LP)DDRn 16GB 2Gx8 1Rx8 5600MHz (non-)ECC (U/R)(SO-)DIMM SDRAM`

where parenthesis denote alternate/optional strings that may be part of the spec.

 > 
 > Just with 4 parenthesis shown above, at least 16 possible valid RAM stick combinations can be achieved. Although not all such combinations of RAM sticks are sold in the market.

We will go through what each spec means, starting from the last:

### DRAM

**Dynamic Random Access Memory** or [DRAM](https://en.wikipedia.org/wiki/Dynamic_random-access_memory) refers to the memory chip, where each bit is stored in a ==memory cell made of a transistor and capactor.==  
This [video](https://youtu.be/CDOOxhRBMIY?list=PL5Q2soXY2Zi-EImKxYYY1SZuGiOAOBKaf&t=5350)  explains the internals of DRAM.

There exists a **Static Random Access Memory** i.e. [SRAM](https://en.wikipedia.org/wiki/Static_random-access_memory) which:

1. is faster but costlier than DRAM
1. uses a set of diodes to store a bit
1. is used in CPU cache.

### SDRAM

**Synchronous DRAM** is any DRAM where the operation of its external pin interface is coordinated by an ==externally supplied clock signal==.  
In older days there used to be **non-synchronous** memory, but no one uses it in modern computers. So the =="S" from the "SDRAM" is almost always dropped==, and we can assume that the any "DRAM" is also synchronous.

==DDRn GDDRn, HBMn etc. are all types of SDRAM.==

Visit [wikipedia](https://en.wikipedia.org/wiki/Synchronous_dynamic_random-access_memory#) page for detailed info.

### DIMM

**Dual inline memory module** refers to the PCB on which DRAM chips are connected together to form a RAM module.

This term ==determines the size of the PCB==.

DIMM comes in various sizes, most famous are:

1. **DIMM 288-pin**: DDR4 and DDR5 SDRAM modules found in PC motherboards
1. **SO-DIMM 260-pin**: DDR4 SDRAM found in Laptops

Visit [Wiki](https://en.wikipedia.org/wiki/DIMM#) for more info.

### Unregistered(U) vs Registered(R)

**Registered memory** (also called **buffered memory**) is computer memory that has a register between the DRAM chips and the system's [memory controller](https://en.wikipedia.org/wiki/Memory_controller "Memory controller").  
A registered memory module ==places less electrical load on a memory controller== than an unregistered one.

Registered memory:

1. ==Is expensive than Unregistered memory (5-6 times)==
1. Mostly used in high-end servers
1. Requires special hardware support (conventional home/work motherboards do not support RDIMM)

**Unregistered memory**  also referred to as unbuffered memory, is what most of the conventional computers support, so often ==the letter "U" from "UDIMM" is also dropped==. You can easily distinguish UDIMM from RDIMM just by looking at the cost.

### ECC vs Non-ECC

**Error Correcting Code** or [ECC](https://en.wikipedia.org/wiki/ECC_memory) memory is a DIMM with extra memory memory chips which add support for error detection and correction of data in RAM.  
Most common ECC modules have 1 extra chip per 8 data chips.

The ECC use a [SECDED codes](https://books.google.co.in/books?id=zJwuDwAAQBAJ&pg=PA95&redir_esc=y#v=onepage&q&f=false) i.e. **Single Error Correcting and Double Error Detecting** which is a modified version of [Extended Hamming Codes](../Security/error_correction.md) technique to detect and correct errors. The ==common configuration is `(72,64,4)`,== where 64 data bits of data is read from the 8 data chips, and 8 bits of parity bits are read from the extra chip.

In ECC memory, the CPU-RAM ==data bus width is 72== rather than typical 64 on non-ECC memory. ==The memory controller reads all 64 data + 8 parity bits from the RAM, and then performs the check.==

Compared to non-ECC, the ECC memory is:

1. Expensive (obviously)
1. More reliable (really though? Need to compare #todo )

In DDR5, each RAM stick is divided into 2 subchannels, where each subchannel has independent data bus. Thus there are 2 types of ECC memory available, **EC4** and **EC8**.  
**EC4** memory has data bus width of 72 (36 per subchannel, 32 data + 4 parity).  
**EC8** memory has data bus width of 80 (40 per subchannel, 32 data + 8 parity).

The ==DDR5 RAM also has a seperate== **On-Chip ECC**. This ECC operates between the memory cells and burst buffers. This uses SECDEC code of size `(136,128,4)`. In `x8` DDR5 SDRAM chip, at each read operations, 128 bits of data from consecutive columns is read, along with 8 parity bits corresponding to those 128 bits. Then the ECC check is performed, and data is then passed to the READ buffer. This **On-Chip ECC** is the lies entirely on the DDR5 chip itself (parity bits are never sent to the memory controller), and this is related to the true ECC discussed before.  
Similarly, GDDR7 also has On-chip ECC.

### The clock speed

The clock speed of the RAM chip, nothing special.

### Rank x Data Width

The term `x8`  in `1Rx8` refers to the number of data pins that each memory chip has for input/output. In `x8`, each chip has data width of 8.  
Similarly, `x4` means data width of 4 bits, `x16` means data width of 16 bits.

Refer to Figures 2-4 of [this datasheet](https://www.mouser.com/datasheet/2/671/16gb_ddr5_sdram_diereva-3193781.pdf) of micron DDR5 memory chips to see the difference between the architecture of chip for different bus widths.

Since a ==CPU expects the data bus width of 64, the data width of each chip determines how many chips must be present on a RAM stick==.  
If I wish to manufacture a RAM stick with 16 GB (128 Gb) of capacity, here's how the I should select the chips:

|Chip Bus Width|Number of chips required|Capacity of each chip required|
|--------------|------------------------|------------------------------|
|x4|16|8 Gb|
|x8|8|16 Gb|
|x16|4|32 Gb|

So with `x16`, we need a chip with higher memory density. This increases the size of the chip. Plus, `x16` also gives performance penalty because it has less number of banks available on a chip (see the Figure 4 of [datasheet](https://www.mouser.com/datasheet/2/671/16gb_ddr5_sdram_diereva-3193781.pdf))  
Similarly, it might be difficult to fit 16 chips on a single RAM stick, which is the case with `x4` chips.

Most commonly used data width is `x8` which gives balance between performance and packaging size.

### Capacity x Number of chips

The term `2Gx8` simply denotes the the RAM stick has 8 chips of 2GB in size.

### DDR

**Double Data Rate** or [DDR](https://en.wikipedia.org/wiki/Double_data_rate) describes a computer bus that ==transfers data on both the rising and falling edges of the clock signal== and hence doubles the memory bandwidth by transferring data twice per clock cycle.

All SDRAM chips are of type DDR.

Some of the most commonly used types of DDR memory are:

1. DDR SDRAM:
   1. Typical, used as CPU memory in desktops/laptops.
   1. Mostly swappable, but some laptop motherboards come with soldered RAM.
   1. To keep the memory module generic, the CPU-RAM data bus width is typically fixed to either 64 (non-ECC) or 72 (ECC) per channel.
   1. Generations: [DDR4](https://en.wikipedia.org/wiki/DDR4_SDRAM),  [DDR5](https://en.wikipedia.org/wiki/DDR5_SDRAM)
1. GDDDR:
   1. A special type of DDR memory designed to be used as GPU memory.
   1. Memory chips are soldered on the same PCB as GPU, so non-swappable.
   1. Since GPU manufacturers have control over the memory chips arrangement, these chips have higher data bus widths than SDRAMs. e.g. NVIDIA RTX 4090 has 384 bit data bus. This allows for higher bandwidths, reaching 1 TB/s
   1. Generations: [GDDR6](https://en.wikipedia.org/wiki/GDDR6_SDRAM) , GDDR7
1. LPDDR:
   1. Low-power DDR memory, used as CPU memory.
   1. Used in mobile phones and power-efficient laptop CPUs (e.g. Apple M1)
   1. Typically soldered on the same PCB as CPU, so non-swappable.
   1. If CPU manufacturer controls the memory arrangement, then the CPU can have larger data bus, achieving higher memory bandwidth. e.g. Apple M3 max has 512-bit data bus, reaching memory bandwidth of 400 GB/s
   1. Generations: [LPPDDR5](https://en.wikipedia.org/wiki/LPDDR#LPDDR5) , LPDDR6

All generational specifications are standardized by an organisation called **JEDEC**.

High Bandwidth Memory or [HBM](https://en.wikipedia.org/wiki/High_Bandwidth_Memory), though not exactly related to DDR, is also another type of memory, which (as the name suggests) has higher bandwidth than DDR or GDDR memories, while using less power.  
This is achieved by stacking the HBM DRAM chips on top of the same substrate as the CPU / GPU. High end HPC GPUs like NVIDIA H100 and AMD MI300X have HBM memory, with data bus width of 5120 or 8196 bits, and a typical bandwidth of 3-8 TB/s.
