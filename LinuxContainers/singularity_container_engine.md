---
aliases:
- Singularity
author: Maneesh Sutar
created: 2023-06-06
modified: 2025-04-14
tags: []
title: Singularity Container Engine
---

# Singularity Container Engine

## Pull

Docker images are stored in layers, so `pull` must also combine those layers into a usable SingularityCE file (.SIF file).

To pull image from dockerhub:

`singularity pull docker://<path>`

To pull from container library (Sylabs)

`singularity pull library://<path>`

pull command creates a new `.sif` file in the current directory.

## Build

To create images from other images or from scratch using a [definition file](#definition-files)  
Also to convert an image between the container formats

e.g. Following commands downloads pre-build images from external sources and converts them to `.sif` format

````sh
singularity build <IMAGE_PATH> docker://<path>
````

## Definition Files

[Doc](https://docs.sylabs.io/guides/latest/user-guide/definition_files.html#definition-files)

Equivalent to Dockerfiles. Standard extension is `.def`.

[Comparision with Dockerfile](https://docs.sylabs.io/guides/latest/user-guide/singularity_and_docker.html#singularityce-definition-file-vs-dockerfile)

A SingularityCE Definition file is divided into two parts:

1. **Header**: describes the **core operating system** to build within the container. Similar to `FROM` in Dockerfile.

1. **Sections**: Similar to layers in Dockerfile. Each section in SIF file is defined by a `%` character followed by the name of the particular section.

## Shell, Exec, Run, Instance Start

The [shell](https://www.sylabs.io/guides/3.11/user-guide/cli/singularity_shell.html) command allows you to spawn a new shell within your container and interact with it as though it were a virtual machine.Once inside of a SingularityCE container, you are the same user as you are on the host system  
Equivalen to `singularity exec <image file path> sh`

The [exec](https://www.sylabs.io/guides/3.11/user-guide/cli/singularity_exec.html) command allows you to execute a custom command within a container by specifying the image file.  
To exec, a command to run MUST be passed.

The [run](https://www.sylabs.io/guides/3.11/user-guide/cli/singularity_run.html) command is same as docker, which will run the container using given image. This is equivalent to `./sif-file-path`. This calls `%runscript` block from the defination file.  
Use `run --containall`  to run a SingularityCE image in an isolated manner:

The [instance start](https://docs.sylabs.io/guides/latest/user-guide/cli/singularity_instance_start.html#singularity-instance-start) command allows you to create a new named instance from an existing container image that will begin running in the background.  Name must be passed as argument after image file path. This calls `%startscript` block from the defination file  
To see list of running containers, `singularity instance list`  
To stop container, `singularity instance stop <name of container>`

By default, Singularity **mounts /home directory to the container.**  
To disable, run with `--no-home`  
To clear env variables, run with `--cleanenv`

## Bind and Mount Directories

Just like Docker, `--bind` and `--mount` commands can be used to mount directories.  
 By default, SingularityCE bind mounts `/home/$USER`, `/tmp`, and `$PWD` into your container at runtime.

## References

1. <https://docs.sylabs.io/guides/latest/user-guide/>
1. <https://biohpc.cornell.edu/doc/singularity_v3.pdf>
