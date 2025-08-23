# Cycle Detection in Graphs

## Introduction
Cycle detection algorithms determine whether a given graph contains cycles—paths where a vertex can be revisited by traversing edges.

## Details
- In directed graphs, cycle detection uses DFS with recursion stack tracking.  
- In undirected graphs, cycle detection is commonly done via DFS with parent tracking or using union-find algorithms.

Detecting cycles is essential for applications like deadlock detection, scheduling, and graph validation.

## Examples
A directed graph with edges creating back edges signifies a cycle.

## Key Concepts
- DFS and recursion stack identify back edges in directed graphs.  
- Parent tracking during DFS identifies cycles in undirected graphs.  
- Union-Find provides efficient cycle detection in undirected graphs.

## Summary
Cycle detection algorithms help ensure structural properties in graphs and prevent inconsistencies.
