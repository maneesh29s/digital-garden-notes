---
aliases: []
author: Maneesh Sutar
created: 2024-04-07
modified: 2025-04-14
tags: []
title: Python Decorators
---

# Python Decorators

Good read: <https://realpython.com/primer-on-python-decorators/>

 > 
 > A decorator is just a regular Python function

You can also define classes as decorators. In this case, such classes must be callable (i.e. need to override `__call__` method).

## Syntactic sugar with @

Python allows to use decorators in a simpler way with the `@` symbol, sometimes called the [pie syntax](https://www.python.org/dev/peps/pep-0318/#background).  
Following code shows example `our_decorator` which wraps a function `func` passed as input.

````python
def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)
    return function_wrapper

def foo_inner(x):
    print("Hi, foo has been called with " + str(x))

foo = our_decorator(foo_inner)

@our_decorator
def foo2(x):
    print("Hi, foo2 has been called with " + str(x))
````

After inspecting the environment variables using `inspect.getmembers(sys.modules[__name__], inspect.isfunction)`, we will get following output

````bash
 ('our_decorator', <function __main__.our_decorator(func)>),
 ('foo_inner', <function __main__.foo_inner(x)>),
 ('foo', <function __main__.our_decorator.<locals>.function_wrapper(x)>),
 ('foo2', <function __main__.our_decorator.<locals>.function_wrapper(x)>),
````

`our_decorator` and  `foo_inner` are regular python functions

While both `foo` and `foo2` are of same type i.e. an instance of function  `our_decorator.function_wrapper`

**This shows that using `@our_decorator` on `foo2` is same as running `foo2 = our_decorator(foo2)`**

But here's a problem, we expected foo2 to be a function of its own type `foo2`, and not of type `function_wrapper`.  
By decorating this (default) way we lose the identity of the wrapped function.

### Sidenote: Its just a syntactic sugar

Consider following lines of code

````python
def wrapper(func):
    print("Inside wrapper with func: ", func)
    return 10 

@wrapper # HINT: same as wrapped = wrapper(wrapped)
def wrapped():
    print("Inside wrapped")
````

Q. If the above code block is executed in a jupyter cell, what will be the output to stdout?

Answer:

````bash
Inside wrapper with func:  <function wrapped at 0x125f86b60>
````

Exaplaination: Since `wrapped` function is not **called** yet, only the print statement from wrapper is executed.

Q. After executing above code block, if we executed following code block, what will be the output?

````python
print(wrapped) 
print(wrapped())
````

Answer:

````bash
10
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[47], line 2
      1 print(wrapped) # outout 1?  
----> 2 print(wrapped()) # output 2? 

TypeError: 'int' object is not callable
````

Explaination:  
`wrapper` returned 10 and it was assigned to `wrapped`. So wrapped, instead of a function, became an integer variable with value 10. Thus `print(wrapped)` returned 10.  
Since integer is not callable, `wrapped()` throws an error

## functools wrap

Python functools provides a convinient way to wrap function in `functools` module called `wrap` and `partial`  
The advantage of using `functools.wraps` is that it **preserves the information of the wrapped function**, such as name, documentation.  
It simply changes the `__name__` , `__doc__` and other relevent variables of the **wrapper** function to be equal to the **wrapped** (inner) function

The decorator has to be modified like this:

````python
from functools import wraps

def our_decorator(func):
    @wraps(func) # same effect as function_wrapper = wraps(func)(function_wrapper)
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)
    return function_wrapper 
````

So now the inspection output is

````python
 ('foo', <function __main__.foo_inner(x)>),
 ('foo2', <function __main__.foo2(x)>),
````

No that even `foo` is not an instance of the `foo_inner`

## functools partial

If the decorator function requires some arguments, then we can't directly use `@decorator` annotation.  
In such cases, decorator can be wrapped inside `@partial`

````python
from functools import wraps, partial

def our_decorator(func, id):
 # id has a local scope. can be accesed inside function_wrapper.
    @wraps(func)
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)
    return function_wrapper

# @our_decorator(2) # will fail
@partial(our_decorator, id = 2)
def foo2(x):
    print("Hi, foo2 has been called with " + str(x))
````
