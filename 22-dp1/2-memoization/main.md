# Memoization

## Introduction

Memoization is an optimization technique used in dynamic programming to speed up recursive algorithms by storing the results of expensive function calls and reusing those results when the same inputs occur again.

## Details

Recursive algorithms often solve the same subproblems multiple times, leading to exponential time complexity. Memoization addresses this by caching the results of calculated subproblems in a lookup table (such as a dictionary or map). When a subproblem is encountered again, the algorithm returns the cached result instead of recomputing it, thus significantly improving performance.

Memoization is typically implemented with a top-down approach, combining recursion with a cache mechanism.

## Examples

The Fibonacci sequence is a classic example where memoization can optimize a naive recursive implementation:

- Naive recursion recalculates Fibonacci numbers multiple times.
- Memoized recursion stores computed values, reducing time complexity from exponential to linear.

Other examples using memoization include:

- Coin change problem
- Calculating factorial with caching
- Calculating lattice paths in grids

## Key Concepts

- **Cache:** A data structure (like a dictionary) to store results of subproblems.
- **Top-down approach:** Recursively solving and caching subproblems.
- **Avoidance of recomputation:** Key advantage of memoization.
- **Improved time complexity:** From potentially exponential to polynomial or linear in many cases.

## Summary

Memoization is a foundational technique in dynamic programming that optimizes recursive algorithms by caching results of subproblems to avoid redundant calculations. It enables efficient solutions to problems that would otherwise be computationally expensive.
