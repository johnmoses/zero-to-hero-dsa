# Two-Dimensional Dynamic Programming Patterns

## Introduction

Two-dimensional (2D) dynamic programming involves problems where the state depends on two parameters, typically represented in a 2D array or matrix. These problems often deal with subsequences, grids, or matrices, requiring solutions that consider combinations of two sequences or dimensions.

## Details

2D DP problems usually arise in scenarios such as string comparison, pathfinding in grids, and other problems where both row and column indices define a subproblem. The main challenge is to carefully define state transitions that depend on previous rows and columns.

Popular 2D DP problems focus on identifying the optimal solution involving pairs of indices, such as longest common subsequence or edit distance between two strings.

## Examples

Classic examples of 2D DP include:

- Longest Common Subsequence (LCS)
- Edit Distance (Levenshtein distance)
- Unique Paths in a grid
- Knapsack problems (2D variant)

These problems demonstrate how to build solutions by iterating over a 2D table, updating entries based on subproblem dependencies.

## Key Concepts

- **State:** Usually defined by two indices (i,j) representing positions in two sequences or dimensions.
- **Transition:** How the current state derives from adjacent or diagonal states.
- **Initialization:** Setting base cases for edges of the DP table.
- **Space optimization:** Possible techniques to reduce memory usage.

## Summary

Two-dimensional dynamic programming is essential for solving problems involving pairs of sequences or grid-based states. Mastering 2D DP patterns equips one to handle complex real-world problems involving strings, matrices, and combinatorics.
