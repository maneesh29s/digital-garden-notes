---
aliases: []
author: Maneesh Sutar
created: 2025-01-18
modified: 2025-04-14
tags: []
title: Graphics Pipeline
---

# Graphics Pipeline

Graphics Pipeline has 3 main components:

1. Vertex Shader: Performs vertex transformations
1. Rasterizer: Fills in the pixels for each visible 2D polygon
1. Fragment Shader: Determines the colors of each pixel

In GPUs, the **Rasterizer** is fixed. That means programmer can not modify the logic of how rasterization is performed.

But programmer can modify the logic of **Vertex** and **Fragment** Shader.  
These are written in a **Shading Language** like [GLSL (OpenGL Shading Language)](https://en.wikipedia.org/wiki/OpenGL_Shading_Language)

These shaders codes are compiled and passed to the GPU, which then performs the necessary computations on the input data.

## Not all GPUs are "graphical"

Data center grade GPUs like Nvidia A100, H100 , do not have display connectors, or Raytracing units, since they are supposed to be used for GPGPU / HPC workloads.

Nvidia's [data center kernel driver](https://docs.nvidia.com/datacenter/tesla/tesla-release-notes-570-86-15/index.html)  are used for both data center GPUs and Quadro GPUs (one with graphical ports). These drivers include libraries for graphics APIs like OpenGL or DirectX. But maybe the nvidia's kernel driver disables these graphics libraries based on the available GPU. (See this video by [LTT](https://youtu.be/zBAxiQi2nPc?t=833) ).

Although TBH, an image in the end is just an array of integers. So you can still write your own algorithms for all components of graphics pipeline. This allows you to run graphic operations on GPUs without graphics capabilties (using all CUDA cores rather than relying on textures units for few tasks).  
This approach is taken in the LBM solver library [FluidX3D](https://github.com/ProjectPhysX/FluidX3D/blob/master/src/kernel.hpp). Here is also a [youtube video](https://youtu.be/pD8JWAZ2f8o?t=757) explaining how FluidX3D works.

## References

1. [Intro to Graphics 07 - GPU Pipeline](https://youtu.be/UzlnprHSbUw?list=PLplnkTzzqsZTfYh4UbhLGpI5kGd5oW_Hh) . This entire playlist of computer graphics lecture is GOLD. This course is more focused on the math behind computer graphics.
1. [Interactive Computer Graphics](https://www.youtube.com/playlist?list=PLplnkTzzqsZS3R5DjmCQsqupu43oS9CFN): A course specifically focused on the computational side of graphics, also talks about modern tools used.
