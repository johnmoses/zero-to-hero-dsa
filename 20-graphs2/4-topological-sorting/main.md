# Topological Sorting

## Introduction
Topological sorting orders the vertices of a directed acyclic graph (DAG) such that for every directed edge (u, v), vertex u comes before vertex v.

## Details
Two main algorithms:

- **DFS-based:** Perform DFS and add vertices to a stack when recursion completes. Reverse the stack for ordering.  
- **Kahn’s Algorithm (BFS-based):** Compute in-degree of each vertex; repeatedly remove vertices with zero in-degree and reduce neighbors' in-degree.

Topological sorting is widely used in scheduling, build systems, and dependency resolution.

## Examples
Task scheduling where some tasks must precede others.

## Key Concepts
- Only applicable to DAGs.  
- DFS and BFS implementations exist.  
- Detects cycle if topological order cannot be completed.

## Summary
Topological sorting provides a linear order respecting dependency constraints in directed acyclic graphs.
