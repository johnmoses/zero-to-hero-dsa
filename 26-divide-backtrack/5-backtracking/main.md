# Backtracking

## Introduction

Backtracking is a general algorithmic technique that incrementally builds candidates to the solutions of a problem and abandons a candidate as soon as it determines that this candidate cannot lead to a valid solution (pruning). It is typically used for solving constraint satisfaction problems.

## Details

Backtracking systematically explores all possible solutions by:

- Building the solution step-by-step.
- Checking at each step if the partial solution is valid.
- Pruning the search space by abandoning invalid partial solutions early.

This approach is often implemented using recursion and is essential in solving combinatorial problems when brute-force checking all possibilities is infeasible.

## Examples

Common problems solved by backtracking:

- N-Queens problem.
- Sudoku Solver.
- Subset Sum and Combination Sum.
- Permutations and combinations generation.

Backtracking can be optimized with heuristics and pruning techniques to improve efficiency.

## Key Concepts

- Recursion with state space exploration.
- Pruning invalid branches early.
- Constraint checking at each step.
- Efficient traversal of large search spaces.

## Summary

Backtracking is a powerful technique for solving problems with large, complex solution spaces by exploring feasible solutions systematically and pruning infeasible ones, enabling solutions to many complex combinatorial problems.
