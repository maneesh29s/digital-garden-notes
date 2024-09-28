---
aliases: []
author: Maneesh Sutar
date: 2023-04-04
tags: []
title: Space Filling Curves
---

# Space Filling Curves

## Pros

1. There is a marginal difference even though index of next position of the curve has to be calculated

## Cons

1. Array has to be padded to a power of 2
1. Parallelism is slightly trickier as the offset of each thread has to calculated
1. It initially looks as if only static scheduling can be done

## Related work

1. Böhm, Christian, Martin Perdacher and Claudia Plant. “A Novel Hilbert Curve for Cache-Locality Preserving Loops.” IEEE Transactions on Big Data 7 (2021): 241-254.

## Example

1. [2D Median Filter with Hilbert Curve](https://gist.github.com/Mark1626/c1f4aebef5b085f74e05b7d3457a3d5b)

## TODO

Try optimising `hilber_inc_xy` function in above gist
