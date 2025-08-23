# Graph Representations

## Introduction
Graphs can be represented in various ways for efficient access and algorithms.

## Details
- **Adjacency Matrix:** NxN matrix with 1 or weight indicating edges. Efficient for dense graphs.  
- **Adjacency List:** List or map of neighbors for each vertex. Efficient for sparse graphs.

Representation choice affects space complexity and algorithm performance.

## Examples
Adjacency lists suit large sparse graphs.

## Key Concepts
- Matrix gives O(1) edge check but uses more space.  
- Lists reduce space at cost of O(degree) edge check.  
- Weighted graphs store weights in place of 1.

## Summary
Selecting suitable representation is crucial for efficient graph processing.
