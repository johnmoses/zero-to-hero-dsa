# Bellman-Ford Algorithm

## Introduction
Bellman-Ford algorithm computes shortest paths from a single source vertex to all other vertices in a weighted graph. It can handle graphs with negative edge weights and detect negative weight cycles.

## Details
- Initializes distances to infinity, except for the source set to zero.  
- Repeatedly relaxes edges |V|-1 times, updating shortest distances.  
- Checks for negative weight cycles by verifying if additional relaxation is possible.

Bellman-Ford is slower than Dijkstra but more versatile due to negative edge handling.

## Examples
Finding shortest paths in graphs where some edges have negative weights but no negative cycles exist.

## Key Concepts
- Edge relaxation is core to shortest path update.  
- Iterative updating ensures correct distances.  
- Negative cycles detection is crucial for correctness.

## Summary
Bellman-Ford is a powerful shortest path algorithm supporting negative weights and cycle detection.
