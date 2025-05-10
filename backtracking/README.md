# Back Tracking

Backtracking is a general algorithm for finding all (or some) solutions to some computational problems (notably Constraint satisfaction problems or CSPs), which incrementally builds candidates to the solution and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot lead to a valid solution.

It is a way of speeding up the search process by removing the most unlikely candidates.

There are two principal ways of using backtracking namely, using stacks or recursion.

## When to use

Use this pattern when you need to find all (or some) solutions to a problem that satisfies given constraints. For example: combinatorial problems, such as generating permutations, combinations, or subsets.

## Problems

Permutations (LeetCode #46)
Subsets (LeetCode #78)
N-Queens (LeetCode #51)
