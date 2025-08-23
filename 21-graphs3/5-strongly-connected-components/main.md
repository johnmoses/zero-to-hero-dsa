# Strongly Connected Components (SCC)

## Introduction
A strongly connected component is a maximal subgraph of a directed graph where each vertex is reachable from every other vertex within that subgraph.

## Details
SCCs can be found using:

- **Kosaraju’s Algorithm:** Performs DFS twice, once on the original graph and once on the reversed graph, processing nodes by finishing times.

- **Tarjan’s Algorithm:** A single pass DFS that uses low-link values and a stack to identify SCCs efficiently.

These algorithms help identify clusters and cycles within directed graphs.

## Examples
Directed graph with nodes grouped into SCCs representing tightly-knit subgraphs.

## Key Concepts
- Reachability within subgraph is mutual.  
- DFS and graph reversal are key components of Kosaraju’s method.  
- Low-link values are core to Tarjan’s method.

## Summary
SCC identification partitions directed graphs into meaningful connectivity clusters for analysis and optimization.
