# Introduction to Dynamic Programming

## Introduction

Dynamic Programming (DP) is a method for solving complex problems by breaking them down into simpler subproblems. It is widely used in algorithm design to optimize recursive solutions by storing the solutions to subproblems to avoid redundant computations.

## Details

DP is applicable when a problem exhibits two key properties:

- **Overlapping Subproblems:** The problem can be broken down into subproblems which are reused multiple times.
- **Optimal Substructure:** The solution to a problem can be constructed efficiently from solutions to its subproblems.

There are two main approaches to DP:

- **Top-Down (Memoization):** Recursion with caching of computed results.
- **Bottom-Up (Tabulation):** Iterative computation and building a table.

DP is commonly used to solve optimization problems, such as finding the shortest path, computing the longest subsequence, and counting combinations.

## Examples

Some classic examples of problems solved using DP:

- Fibonacci sequence calculation.
- Coin change problem.
- Longest Common Subsequence.
- 0/1 Knapsack problem.

These problems show how naive recursive approaches can be improved to run efficiently using DP techniques.

## Key Concepts

- **Memoization:** Caching results of recursive function calls.
- **Tabulation:** Solving problems iteratively by filling a DP table.
- **State and Transition:** Defining the parameters that represent the problem state and how states relate.
- **Time and Space Complexity:** DP often reduces exponential time to polynomial time but may require additional memory.

## Summary

Dynamic Programming is a systematic way to solve problems involving overlapping subproblems and optimal substructure by storing intermediate results. This introduction lays the foundation for learning memoization, tabulation, and common DP problem patterns.
