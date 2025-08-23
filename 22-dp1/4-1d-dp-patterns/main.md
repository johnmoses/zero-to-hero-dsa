# One-Dimensional Dynamic Programming Patterns

## Introduction

One-dimensional (1D) dynamic programming involves problems where the state can be represented with a single parameter, often an index. These problems typically use a one-dimensional array (or list) to store intermediate results, making solutions efficient and easier to implement.

## Details

1D DP problems often involve sequences or linear structures such as arrays or strings. The core idea is to define a state that represents a solution to a subproblem based on a position or size and then build upon smaller states to solve larger ones.

Common examples include problems related to counting, optimization, and subsequences. Key to solving these problems efficiently is identifying the recurrence relation and knowing how to iteratively compute the DP array.

## Examples

Typical 1D DP problems include:

- Climbing Stairs: Counting distinct ways to reach the top.
- Maximum Subarray Sum: Finding a contiguous subarray with the maximum sum.
- House Robber: Maximizing sum without robbing adjacent houses.
- Fibonacci sequence using tabulation or memoization.

These problems showcase how to transition from smaller subproblems (like previous indices) to larger ones.

## Key Concepts

- **State definition:** Usually index-based.
- **Transition:** How each state relates to previous states.
- **Base cases:** Initial subproblems with known solutions.
- **Space optimization:** Many 1D DP problems can be optimized to use constant space.

## Summary

One-dimensional DP patterns are fundamental in many algorithmic problems involving sequences. Mastering these patterns builds a strong foundation for more complex DP problems encountered in higher dimensions or generalized
