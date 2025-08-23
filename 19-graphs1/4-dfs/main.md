# Depth-First Search (DFS)

## Introduction
Depth-First Search (DFS) is a graph traversal algorithm that explores as far as possible along each branch before backtracking. It is used to visit all nodes of a graph in a depthward motion.

## Details
DFS can be implemented recursively or iteratively using a stack. It marks visited nodes to avoid revisiting and cycles.

Key operations:
- Start at a source node.
- Visit the node and recursively explore each unvisited neighbor.
- Backtrack when no unvisited neighbors remain.

DFS helps in path finding, cycle detection, topological sorting, and exploring connected components.

## Example
Given a graph, DFS visiting order starting from node "A" might be: A, B, D, C.

## Key Concepts
- Uses recursion or stack for traversal.
- Requires tracking of visited nodes.
- Explores deep before broad in the graph.

## Summary
DFS is fundamental for deep exploration in graphs, enabling many graph algorithms.
