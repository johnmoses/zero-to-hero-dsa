# Dijkstra's Algorithm for Shortest Path

## Introduction
Dijkstra’s algorithm finds the shortest paths from a single source node to all other nodes in a graph with non-negative edge weights.

## Details
- Initialize distances to infinity except the source vertex set to zero.  
- Use a priority queue (min heap) to greedily select the minimum distance unvisited vertex.  
- Update distances to neighbors if a shorter path is found through the selected vertex.  
- Repeat until all nodes are visited or distances finalized.

Dijkstra’s algorithm does not work with negative edge weights.

## Examples
Routing protocols and pathfinding in GPS systems commonly use Dijkstra.

## Key Concepts
- Greedy selection of closest vertex.  
- Distance updates reflect the shortest known path.  
- Uses priority queue for efficiency.

## Summary
Dijkstra's algorithm efficiently computes shortest path trees for graphs with non-negative edges.
