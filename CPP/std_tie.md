---
aliases: []
author: Maneesh Sutar
created: 2023-11-23
modified: 2025-04-14
tags:
- cpp
title: C++ std::tie
---

# C++ std::tie

for destructuring tuples returned from a function

````cpp

std::tuple<int,int> func() {  
return std::tuple(3,4)
}

std::tie(val1, val2) = func();
// val1 = 3
// val2 = 4

````

supported since c++11
