# Tabulation

## Introduction

Tabulation is a dynamic programming technique that solves problems in a bottom-up manner by iteratively filling a table (usually an array or matrix) based on previously computed values. It avoids recursion and builds the solution by solving all subproblems beginning from the smallest.

## Details

Unlike memoization, which uses a top-down recursive approach with caching, tabulation starts from the base cases and works upward, filling a table with solutions to subproblems. This approach often simplifies the logic, avoids recursion overhead, and can use less memory in certain cases.

Tabulation requires a well-defined order of solving smaller subproblems before the larger problem, by establishing dependencies between subproblems.

## Examples

A classical example of tabulation is computing the Fibonacci sequence:

- Create an array to store Fibonacci values up to n.
- Initialize base cases (fib[0] = 0, fib = 1).
- Iteratively compute fib[i] = fib[i-1] + fib[i-2] for i from 2 to n.

Other examples include:

- Computing ways to climb stairs.
- Coin change using tabulation.
- Longest common subsequence.

## Key Concepts

- **Bottom-up computation:** Solve smaller subproblems first.
- **Table construction:** Use arrays or matrices to store results.
- **No recursion:** Avoids function call overhead.
- **Order of evaluation:** Important to handle dependencies correctly.
- **Efficiency:** Time complexity often linear or polynomial based on problem.

## Summary

Tabulation is a core dynamic programming approach that builds solutions iteratively by solving all relevant subproblems first. This bottom-up method complements memoization and is often more straightforward to implement for many problems.
