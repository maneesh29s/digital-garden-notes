---
aliases: []
author: Maneesh Sutar
date: 2024-04-12
tags:
- public
- cpp
title: Smart Pointers
---

# Smart Pointers

Good video: <https://youtu.be/UOB7-B2MfwA>  
Their purpose is **only to create new objects** and not to point to existing objects

Please refer to the code examples which also include comments for better understanding:

* [smart pointers](https://github.com/maneesh29s/just-cpp-things/blob/main/src/smart_pointers.cc)

## Unique pointers

<https://en.cppreference.com/w/cpp/memory/unique_ptr/>  
Creates new object, and gives a **unique pointer** to that object  
Smart Pointer entirely owns the object  
**object is deleted when the unique pointer is out of scope**  
Copy Constructor and operator of `unique_ptr` is explicitly deleted

must use **move** symantics, if

1. need to pass to a function / constructor
1. need to create annother unique pointer but pointing to same object

<https://en.cppreference.com/w/cpp/memory/unique_ptr/make_unique>  
Use `make_unique` to create the object in a safer way (error handling while constructing), then pass it to `unique_ptr`  
Else we can also directly pass `new Object()` in the constructor of `unique_ptr`, might create dangling pointer if constructor of object threw some error

## Shared pointers

<https://en.cppreference.com/w/cpp/memory/shared_ptr>  
Creates new object, and gives a pointer to that object  
Pointer can be copied to another pointer  
Pointer can be passed to a function / constructor with copy symantics  
The `shared_ptr` **keeps track of how many total pointer point** to the same data  
**object is deleted when  all the pointers are out of scope**

<https://en.cppreference.com/w/cpp/memory/shared_ptr/make_shared>  
**Must** use `make_shared` to generate object and pass it to `shared_ptr` constructor

### Weak Pointer

<https://en.cppreference.com/w/cpp/memory/weak_ptr>  
**Points to a already defined shared_ptr**  
**But does not increase pointer count of `shared_ptr`**  
So its possible, that `weak_ptr` is pointing to an object that is deleted since all its `shared_ptr` were out of scope  
In such case, we must first check if `weak_ptr` is valid using provided methods

### About make_shared and make_unique

make\_unique\<T>(args) and make\_shared\<T>(args) pass the "args" to one of the valid constructors of type T.  
They will always create a new object which the smart pointer owns.  
even if you pass an existing object, they will either call "copy constructor" or "move constructor".  
But they will not point to existing object.
