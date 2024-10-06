---
aliases: []
author: Maneesh Sutar
created: 2023-06-16
modified: 2024-09-28
tags:
- metaprogramming
- cpp
title: Template Metaprogramming in C++
---

# Template Metaprogramming in C++

Its just another programming paradigm

Basically, all the computation is done at compile time itself.  
This will increase compilation time, but runtime will be reduced.

In c++ we use templates to perform this.

For e.g. following program computes 2^8

````cpp
#include <iostream>
using namespace std;
 
template<int n> struct funStruct
{
    enum { val = 2*funStruct<n-1>::val };
};
 
template<> struct funStruct<0>
{
    enum { val = 1 };
};
 
int main()
{
 // 8 is passed during compilation itself
    cout << funStruct<8>::val << endl;
    return 0;
}
````

<https://en.wikibooks.org/wiki/C%2B%2B_Programming/Templates/Template_Meta-Programming#History_of_TMP>

## Practical Usecases

1. When computation in your code is not dependent on runtime values
1. Implmentation of std::tuple uses template metaprogramming
1. Boost library functions use template meta programming

## Personal Opinion

Still don't understand why and when this paradigm will be useful, since it can not handle values inputed at runtime

## Advanced Video Series

<https://www.youtube.com/playlist?list=PLWxziGKTUvQFIsbbFcTZz7jOT4TMGnZBh>
