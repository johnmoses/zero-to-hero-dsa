# Minimum Spanning Trees (MST)

## Introduction
A Minimum Spanning Tree connects all vertices in a weighted undirected graph with the minimum total edge weight, and without cycles.

## Details
Prim's algorithm is a greedy approach:
- Start from an arbitrary vertex.  
- Use a priority queue to select the minimum weight edge connecting the MST to a new vertex.  
- Add the vertex and edge to the MST and repeat until all vertices included.

MSTs are essential in network design, clustering, and minimizing infrastructure cost.

## Examples
Constructing an MST of a graph representing a network's cable layout with minimal total length.

## Key Concepts
- Greedy selection of minimum edges.  
- Priority queue improves edge selection efficiency.  
- Avoid cycles by only connecting new vertices.

## Summary
Prim's algorithm efficiently constructs MSTs, optimizing weighted connectivity.
