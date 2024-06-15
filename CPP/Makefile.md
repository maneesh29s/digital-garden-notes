---
aliases: []
author: Maneesh Sutar
date: 2024-03-28
tags:
- public
- cpp
title: Makefile
---

# Makefile

## Syntax

A ***Rule*** in makefile looks like this:

````makefile
targets: prerequisites
 recipe
````

 > 
 > Typically, the recipe operates of pre-requisites (other targets/files) and produces a new file with same name as current target

MUST USE TABS, not spaces

## Recipe

A *recipe* is an action that `make` carries out.  
*A recipe may have more than one command*, either on the same line or each on its own line

Ref: <https://makefiletutorial.com/>

**Each command is run in a new shell (or at least the effect is as such)**

````bash
all: 
    cd ..
    # The cd above does not affect this line, because each command is effectively run in a new shell
    echo `pwd`

    # This cd command affects the next because they are on the same line
    cd ..;echo `pwd`

    # Same as above
    cd ..; \
    echo `pwd`
````

## Multiple Targets and Default Target

There can be multiple targets in the same Rule. `$@` automatic variable autoamtically **picks the target name which is being called**

**The very first target in the file is the default target**. It runs when you only call `make` with no arguments

## What does running a target mean?

Assume **X** is a target in the Makefile

It will be run when:

1. It is called diretly using `make X`
1. X is a pre-requisite of another target say **Y**

Once target is run:

1. If the commands in the target **X** do not create a file **X**, then `make` will run the recipe in the target **X** **everytime**. This behaviour is similar to `.PHONY`
1. If **X** is an existing file in the repo, then `make` will first check if the existing file **X** is outdated or not. If its outdated, `make` will run the recipe in the target **X**

## How does make verify if files are outdated?

Ref: <https://makefiletutorial.com/>

To make this happen, it uses the filesystem timestamps as a proxy to determine if something has changed. This is a reasonable heuristic, because file timestamps typically will only change if the files are modified. But it's important to realize that this isn't always the case. You could, for example, modify a file, and then change the modified timestamp of that file to something old. If you did, Make would incorrectly guess that the file hadn't changed and thus could be ignored.

## Variables

**Variables** can be initialised with either `:=` or `=`  
`files := file1 file2`  
Single or double quotes have no meaning to Make, they are simply characters that are assigned to the variable  
but those might be meaningful to bash

## Automatic Variables

<https://www.gnu.org/software/make/manual/html_node/Automatic-Variables.html>

NOTE: **they only have values within the recipe**. In targets/prerequisites they will resolve to empty strings.

````bash
# outputs the active target name
$@

# all prerequisites newer than the target
$?

# Outputs all prerequisites with spaces
$^

# The name of the first prerequisite.
$<

````

## Wildcards

`*` and `%` are some of the wildcard symbos, used for autocompletion.

`*` searches your filesystem for matching filenames.  
`*` may be used in the target, prerequisites, variable assignment or in the `wildcard` function.  
For safety, always use it with  `wildcard` function, e.g. `$(wildcard *.o)`

`%` wildcard is used for matching and replacing  
`%` is most often used in rule definitions and in some specific functions.

## Dependency files

Note: #todo not sure why we do it clear purpose

<https://stackoverflow.com/questions/19114410/what-is-d-file-after-building-with-make>

More details can be found gcc documentation for preprocessor args: [link](https://gcc.gnu.org/onlinedocs/gcc/Preprocessor-Options.html#index-M)

Usually, `-MD` or `-MMD` is used to generate a dependency output file as a side effect of the compilation process

## References

1. <https://makefiletutorial.com/>
