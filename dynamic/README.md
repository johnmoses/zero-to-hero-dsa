# Dynamic Programming

Dynamic programming is an algorithmic technique that optimizes solutions to problems exhibiting overlapping subproblems and optimal substructure properties. It avoids recomputing solutions by storing and reusing them, typically using memoization (top-down) or tabulation (bottom-up) approaches.

## General Pattern

Identify Subproblems:
Break down the main problem into smaller, overlapping subproblems.

Define Recurrence Relation:
Express the solution to a subproblem in terms of solutions to smaller subproblems.

Base Cases:
Define the solutions to the simplest subproblems that can be solved directly.

## Memoization or Tabulation

Memoization (Top-Down): Store the results of solved subproblems in a dictionary or array. Before solving a subproblem, check if it's already solved and reuse the stored result.
Tabulation (Bottom-Up): Build a table (usually an array) of solutions to subproblems, starting from the base cases and working up to the final solution.

Return the Solution:
Extract the final solution from the memoization table or the last entry of the tabulation table.

## Common Patterns

1D DP:
Problems that can be solved using a single array to store subproblem solutions. Examples include Fibonacci sequence, climbing stairs, and maximum subarray sum.

2D DP:
Problems that require a 2D array (matrix) to store subproblem solutions. Examples include longest common subsequence, edit distance, and matrix chain multiplication.

Subset/Combination Problems:
Problems that involve finding subsets or combinations that satisfy certain conditions. Examples include coin change, knapsack problem, and partition equal subset sum.

## When to use

Use this pattern for problems with overlapping subproblems and optimal substructure.

## Problems

- Climbing Stairs (LeetCode #70, Blind, Grind)
- Maximum Subarray Sum (LeetCode #53, Grind)
- Coin Change (LeetCode #322, Blind, Grind)
- Partition Equal Subset Sum (LeetCode #416, Grind)
- House Robber (LeetCode #198, Blind)
- House Robber II (LeetCode #213, Blind)
- Longest Increasing Subsequence (LIS) (LeetCode #300, Blind)
- Longest Common Subsequence (LeetCode #1143, Blind)
- Unique Paths (LeetCode #62, Blind)
- Word Break (LeetCode #139, Blind)
- Combination Sum (LeetCode #39, Blind)
- Decode Ways to Decode (LeetCode #91, Blind)
- Fibonacci Sequence (LeetCode #509)
- Edit Distance (LeetCode #72)
- Matrix Chain Multiplication (LeetCode #354)
- Jump Game (LeetCode #55)
