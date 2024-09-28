---
aliases:
- Nextflow
author: Maneesh Sutar
date: 2023-05-08
tags: []
title: Nextflow
---

# Nextflow

<https://www.nextflow.io/docs/latest/getstarted.html>

**process** - basic processing unit (maybe a stage)

**channels/queues** - data input and output streams of sort

**watchPath** - for a watch on file events

**script**: (script block) can be a string or groovy code that returns a string

`‘ ’ / ” ” / ’’’ ‘’’ / ””” “””`

bash-like variable expansion in single vs double quote (variables defined in nexflow file scope)  
for system variables use single quotes

**exec**: (exec block) groovy code to be executed

## ErrorStrategies

‘retry’ - more exploration needed

‘maxRetries’ - number of retries for an instance of a process (or can be called a task)

‘maxErrors’ - number of errors for all instances of a process (all tasks)

**stages** - processes

**supported languages** - shebang in the script

## Nextflow variables

`!varName is nextflow variable in shell ($varName is bash variable in shell)`

`$varName is valid everywhere`

## Workflow

Workflow is where it starts  
processes are run in workflow and can be pipelined as per the need  
input and output channels can be used to chain processes together  
scripts are where the execution happens, can be bash, python or any other scripting language

<https://carpentries-incubator.github.io/workflows-nextflow/08-configuration/index.html>
