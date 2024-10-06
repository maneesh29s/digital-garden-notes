---
aliases: []
author: Maneesh Sutar
created: 2024-06-02
modified: 2024-09-28
tags:
- cpp
title: CPP Tricks
---

# CPP Tricks

## which is faster: 2 for loops or a combined single loop?

````cpp

for (i in size) 
 x[i] = x[i] + 2;

for (i in size)
 y[i] = y[i] + 2;

````

OR

````cpp
for (i in size) {
x[i] = x[i] + 2;
y[i] = y[i] + 2;
}
````

It depends on what the operation is being performed in the loop

**First can be faster, since compiler can optimise the loop with SIMD if the operation is simple.**
