# Union Find (Disjoint Set Union)

## Introduction

Union Find, also known as Disjoint Set Union (DSU), is a data structure that keeps track of elements partitioned into disjoint sets. It supports efficient union and find operations used to manage connectivity and component grouping problems.

## Details

Key operations:

- **Find:** Determine which set an element belongs to.
- **Union:** Merge two sets into one.

Union Find is widely used in problems that involve connectivity, such as network connectivity, cycle detection in graphs, and clustering.

Optimizations include:

- **Path Compression:** Shortens the paths in the find operation.
- **Union by Rank/Size:** Attaches the smaller tree under the root of the larger tree to keep the tree shallow.

With these optimizations, Union Find operations work in almost constant amortized time.

## Examples

Applications:

- Detecting cycles in an undirected graph.
- Kruskal’s Minimum Spanning Tree algorithm.
- Finding connected components.

## Key Concepts

- Disjoint sets representation with parent pointers.
- Efficient union and find with path compression.
- Amortized inverse Ackermann time complexity.
- Use cases in graph algorithms.

## Summary

Union Find is a fundamental data structure for dynamically managing disjoint sets and connectivity queries, essential for many graph and clustering
