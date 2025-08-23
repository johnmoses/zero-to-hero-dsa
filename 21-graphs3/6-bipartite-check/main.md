# Bipartite Graph Check

## Introduction
A bipartite graph is a graph whose vertices can be divided into two disjoint sets such that every edge connects a vertex from one set to a vertex from the other set. There are no edges connecting vertices within the same set.

## Details
Checking if a graph is bipartite is equivalent to checking whether it is two-colorable — if the graph's vertices can be colored with two colors such that no adjacent vertices have the same color.

### BFS Approach:
- Start BFS from any uncolored vertex, assign it a color (e.g., 0).  
- Assign the opposite color to its neighbors (e.g., 1), continuing in BFS order.  
- If at any point a neighbor has the same color as the current vertex, the graph is not bipartite.  
- Repeat for all connected components.

If no conflicts arise, the graph is bipartite.

## Examples
Graphs containing an odd length cycle are not bipartite.

## Key Concepts
- Bipartite means no edges link vertices of the same color.  
- BFS or DFS can be used to check bipartiteness efficiently.  
- Cycle length parity (even) affects bipartiteness.

## Summary
Bipartite checks enable applications like graph partitioning, matching, and scheduling.
