---
aliases: []
author: Maneesh Sutar
date: 2024-02-12
tags: []
title: JAX
---

# JAX

Jax follows [Functional Programming](../FunctionalProgramming/functional_programming.md)  
Works great with [Pure Functions](../FunctionalProgramming/pure_functions.md)

For impure functions, it may produce unexpected results or errors.

## Jax arrays

Numpy arrays are mutable, but **jax arrays are immutable**.  
To modify the arrays we need to use a `at` syntax.

|Alternate syntax|Equivalent In-place expression|
|----------------|------------------------------|
|`x = x.at[idx].set(y)`|`x[idx] = y`|
|`x = x.at[idx].add(y)`|`x[idx] += y`|
|`x = x.at[idx].multiply(y)`|`x[idx] *= y`|
|`x = x.at[idx].divide(y)`|`x[idx] /= y`|
|`x = x.at[idx].power(y)`|`x[idx] **= y`|
|`x = x.at[idx].min(y)`|`x[idx] = minimum(x[idx], y)`|
|`x = x.at[idx].max(y)`|`x[idx] = maximum(x[idx], y)`|
|`x = x.at[idx].apply(ufunc)`|`ufunc.at(x, idx)`|
|`x = x.at[idx].get()`|`x = x[idx]`|

None of the x.at expressions modify the original x; instead ==they return a modified copy of x==. However, inside a jit() compiled function, expressions like x = x.at\[idx\].set(y) are guaranteed ==to be applied in-place==.  
Every function can take some optional parameters mentioned [here](https://jax.readthedocs.io/en/latest/_autosummary/jax.numpy.ndarray.at.html)

## Out of bound index

Raising an error from code running on an accelerator can be difficult or impossible. Therefore, JAX must choose some non-error behavior for out of bounds indexing (akin to how invalid floating point arithmetic results in `NaN`)

e.g. reading the closest in-bound element, skipping write operations on out-of-bound elements  
You can use the optional parameters of [`ndarray.at`](https://jax.readthedocs.io/en/latest/_autosummary/jax.numpy.ndarray.at.html) to get finer control

## JIT

Just in time compilar for JAX  
We can use `@jit` annotation above any jax-python function to be compiled

Read more on JIT in my [medium blog](https://medium.com/e4r/feature-toggle-in-jax-109541290c68)

### static_arguments

 using the `static_argnums` argument to `jit`, we can specify to trace on concrete values of some arguments

### donate_arguments

If you know that one of the inputs is not needed after the computation, and if it matches the shape and element type of one of the outputs, you can specify that you want the corresponding input buffer to be donated to hold an output.

````py
def add(x, y):
  return x + y

x = jax.device_put(np.ones((2, 3)))
y = jax.device_put(np.ones((2, 3)))
# Execute `add` with donation of the buffer for `y`. The result has
# the same shape and type as `y`, so it will share its buffer.
z = jax.jit(add, donate_argnums=(1,))(x, y)
````

### Static vs Traced operations

<https://jax.readthedocs.io/en/latest/notebooks/thinking_in_jax.html#jit-mechanics-tracing-and-static-variables>

* Just as values can be either static or traced, operations can be static or traced.
* Static operations are evaluated at compile-time in Python; traced operations are compiled & evaluated at run-time in XLA.
* Use `numpy` for operations that you want to be static; use `jax.numpy` for operations that you want to be traced.

## Vectorised Evaluation

Runs given JAX program across

1. ==Multiple threads in GPU/TPU==
1. ==Multiple threads in CPU==  
   Implemented using [`jax.vmap`](https://jax.readthedocs.io/en/latest/_autosummary/jax.vmap.html)  
   The available device to execute can be found out using [`jax.local_devices`](https://jax.readthedocs.io/en/latest/_autosummary/jax.local_devices.html)

If "N" number of nested `vmap` are applied on a function, then the function can be run on an array with N-dimensions.  
At each `vmap` you can also specify which dimension to vectorize on.

## Parallel Evaluation (Single Host)

[Source](https://jax.readthedocs.io/en/latest/jax-101/06-parallelism.html)  
JAX for **single-program, multiple-data (SPMD)** code.

==Single program running on the host (CPU)==, input data is ==distributed across connected== [local devices](https://jax.readthedocs.io/en/latest/_autosummary/jax.local_devices.html) (multiple GPUs or TPUs), and output from all devices is returned back to host CPU.

Implemented using [`jax.pmap`](https://jax.readthedocs.io/en/latest/_autosummary/jax.pmap.html)  
`jax.pmap` can also be combined with `jax.vmap` to run vectorised code across multiple threads inside each GPU/TPU

### Pre-requisites

1. Input data which is to be shared across multiple devices ==needs to be batched== i.e. the size of first dimension of the array = number of local device

## Distributed Evaluation (Multi Host)

[Ref](https://jax.readthedocs.io/en/latest/multi_process.html)

Running **single-program, multiple-data (SPMD)** code, on **multi-host (multi-CPU) clusters**

### Pre-requisites

* Need to **mannually** run **one JAX process per host (CPU)** . Each process runs independently in a multi-controller mode.

* Must initialize the cluster with [`jax.distributed.initialize()`](https://jax.readthedocs.io/en/latest/_autosummary/jax.distributed.initialize.html#jax.distributed.initialize "jax.distributed.initialize") (similar to MPI_Init())

### Local vs Global Devices

A process’s local devices are those that it can directly address and launch computations on.  
You can see a process’s local devices via [`jax.local_devices()`](https://jax.readthedocs.io/en/latest/_autosummary/jax.local_devices.html#jax.local_devices "jax.local_devices") .

The global devices are the devices across all processes. You can see all available global devices via [`jax.devices()`](https://jax.readthedocs.io/en/latest/_autosummary/jax.devices.html#jax.devices "jax.devices")

==A process’s local devices are always a subset of the global devices.==

### Communication across devices

1. Use collective communication operations (e.g. [`jax.lax.psum()`](https://jax.readthedocs.io/en/latest/_autosummary/jax.lax.psum.html#jax.lax.psum "jax.lax.psum") ) in multi-process settings. This will take care of all local/global device communications.
1. Other communication methods depending on your use case (e.g. RPC, [mpi4jax](https://github.com/mpi4jax/mpi4jax)).

### MPI equivalent functions

1. [`jax.process_index`](https://jax.readthedocs.io/en/latest/_autosummary/jax.process_index.html#jax-process-index): Returns the integer process index i.e. **rank** of this process.
1. [`jax.process_count`](https://jax.readthedocs.io/en/latest/_autosummary/jax.process_count.html#jax-process-count): Returns the number of JAX processes associated with the backend i.e. **size**.

## CUDA for Custom operations for GPUs

 JAX allows users to define custom operations for GPUs (single or multi)

Read more:

* <https://jax.readthedocs.io/en/latest/Custom_Operation_for_GPUs.html>
* <https://github.com/dfm/extending-jax>

## Convolutions in JAX

Image convolutions using functions present in `jax.numpy`, `jax.scipy` and `jax.lax`

Read more:

* <https://jax.readthedocs.io/en/latest/notebooks/convolutions.html>

## Shard map

Read more:

* <https://jax.readthedocs.io/en/latest/notebooks/shard_map.html>
* <https://jax.readthedocs.io/en/latest/notebooks/Distributed_arrays_and_automatic_parallelization.html#distributed-arrays-and-automatic-parallelization>
