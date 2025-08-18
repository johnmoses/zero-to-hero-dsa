# Greedy Programming

A greedy algorithm is a type of technique or approach that follows the problem-solving heuristic of making the locally optimal choice at each stage with the hope of finding a global optimum. In other words, at each step, it chooses the option that seems the best at that moment without considering the potential impact of the decision on future steps.

Greedy programming is mainly used for optimization problems where the goal is to find the best solution among a set of possibilities. The solutions are constructed incrementally, with the algorithm making the locally optimal choice at each stage.

## When to Use a Greedy Approach

A problem can be solved using a greedy approach if it has the following properties:

1.  **Greedy Choice Property:** A global optimal solution can be arrived at by making a locally optimal choice. In other words, the choice made at each step does not depend on future choices.
2.  **Optimal Substructure:** An optimal solution to the problem contains an optimal solution to its subproblems.

## General Steps to a Greedy Algorithm

1.  **Identify the optimal substructure:** Break the problem down into smaller, independent subproblems.
2.  **Develop a recursive solution:** Define a recursive relationship to solve the subproblems.
3.  **Make a greedy choice:** At each step, make the choice that seems the best at the moment.
4.  **Prove that the greedy choice is safe:** Show that the greedy choice will lead to a globally optimal solution.
5.  **Develop a recursive algorithm that implements the greedy strategy.**
6.  **Convert the recursive algorithm to an iterative algorithm.**

## Problems

### Jump Game (LeetCode #55)

**Problem:** Given an array of non-negative integers, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Determine if you are able to reach the last index.

**Greedy Approach:** The greedy approach is to keep track of the maximum reach from the current position. At each position, we update the maximum reach. If the current position is beyond the maximum reach, it means we cannot reach the end.

### Merge Intervals (LeetCode #56)

**Problem:** Given a collection of intervals, merge all overlapping intervals.

**Greedy Approach:** The greedy approach is to sort the intervals by their start times. Then, iterate through the sorted intervals and merge any overlapping intervals.

## Limitations of Greedy Algorithms

Greedy algorithms do not always produce the optimal solution. The choice made at each step is based on the information available at that moment, and it may not be the best choice in the long run. For example, the greedy approach may not work for the 0/1 Knapsack problem, where it is better to use dynamic programming.