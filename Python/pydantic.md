---
aliases: []
author: Maneesh Sutar
created: 2024-04-08
modified: 2024-09-28
tags: []
title: Pydantic
---

# Pydantic

[Pydantic Documentation](https://docs.pydantic.dev/latest/)  
A good page [comparing all the python dataclass](https://www.attrs.org/en/stable/why.html) libraries

Is a **data validation** library.  
it can generate data classes, similar to python's own dataclases module, but it also **validates the data types of the attributes** of the dataclass.

Pydantic provides many pre-defined validation types, like:

1. primitives: int, str, float
1. custom: EmailStr, PositiveFloat

You can also create your own validator function.  
To do this, add `@validator` decorator to the function defined in your data class

**Pydantic uses inheritance** to define data classes. `attr` library uses decorators

v1 and v2 have same features, only some of the APIs have changed.  
Expecting to use v2 if you are new user, no need to migrate from v1 to v2
