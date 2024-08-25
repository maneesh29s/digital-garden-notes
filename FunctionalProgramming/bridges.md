---
aliases: []
author: Maneesh Sutar
date: 2023-11-12
tags:
- functionalProgramming
- clojure
- public
title: Bridges in Functional Programming
---

# Bridges in Functional Programming

Functional Programming languages have their own way to handle [Side-effects](side_effects.md), while minimising their impact

e.g.  
Clojure, has "Atoms", which are mutable variables

Agents / Actors:  
Maintain a queue of actions to perform on the outside world
