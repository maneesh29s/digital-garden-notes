---
aliases:
- Pure Functions
author: Maneesh Sutar
created: 2023-11-12
modified: 2024-09-28
tags: []
title: Pure Functions
---

# Pure Functions

Its just a way to write methods.

In Mathematics, functions always produce the same output for a given set of inputs.

In [Functional Programming](functional_programming.md) world, a pure function:

1. For a given input, will always produce the same output.
1. should not produce any [Side-effects](side_effects.md)

Have have look the function `add` in following example:

 > 
 > Remember: We are just going to understand what a pure function can / can not do. The "logic" and the "effect/output" across all the code snippet will vary

````python
y = 5

def add(x):
 y += x 

# function calls
add(5); # y == 10
add(5); # y == 15 
# same input, different output
# not allowed in FP
````

The issue is that **the function is dependent on/modifying a state which is outside its own scope**.  
This is an example of [Side-effect](side_effects.md)

What about the following implementation of `add` ?

````python
def add (x, y){
 return x + y
}

y = 5
# function calls
add(y, 5); # 10
add(y, 5); # 10
# same input, same output
````

All good right?  
Now let's do a slight modification

````python
def add ( x, y) {
 return x + y
}

y = 5
# function calls
add(y, 5); # 10

# 100 lines of code
y = 20 # oh no somebody changed the variable
# 100 lines of code

add(y, 5); # 25
# same input, different output
````

The issue is that the original variable `y` is mutable. And it will be hard to see where the `y` is getting mutated if you have 100s of lines of code in between.

To solve this, **make all variables immutable**  
Every function will always return a new variable or copy of the existing variable.

You can see the issue here, **COPIES !!**

Consider an example:

````python
def update (arr, index, value): # arr is immutable
 new_arr = arr # need to make a mutable copy of arr
 new_arr[index] = valu
 return new_arr
````

So just to modify a single value, we need to create a deep copy of the whole input array.

This looks insane, but in reality, Functional Programming languages implement  
[persistent_data_structures](persistent_data_structures.md), which can avoid deep copies and perform efficiently.
