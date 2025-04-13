---
aliases:
- Side-effects
author: Maneesh Sutar
created: 2023-11-12
modified: 2025-04-14
tags: []
title: Side-Effects in Functional Programming
---

# Side-Effects in Functional Programming

In [Functional Programming](functional_programming.md), when a function modifies a state outside of its scope,  this behaviour is called as a Side-effect

Examples of Side-effects

1. Modifying inputs (think of pointers or references, or arrays)
1. Modifying global variables
1. printing to console
1. HTTP calls
1. Changing the filesystem
1. Querying the DOM

**See in real world, you can not avoid side effects entirely.**

In most cases, your whole applications are built to do HTTP calls or database updates.

And in many cases you need to have **mutable variables** shared between multiple threads e.g. counters.

To tackle this FP languages have [bridges](bridges.md)
