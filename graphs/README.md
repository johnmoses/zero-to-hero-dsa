# Graphs

A graph is a set of objects called `vertices`, together with a collection of pairwise connections between them called `edges`. It is a way or representing relationships between pairs of objects.

Practical examples of graphs are city maps, airline routes, electrical wiring mappings, link between web pages, relationship between students and courses, communication network diagram.

The vertices are also called `nodes` while the edges are also called `arcs`. The edges can be described as `directed` if they are ordered and `undirected` if they are not ordered, and `unidirected` if all edges are undirected.

The vertices and edges may also be `labeled` or `unlabeled`. When the edges are labeled with numbers, the numbers can be viewed as `weights`, and the graph is said to be a `weighted`
graph.

## Paths

Paths are a sequence of nodes for moving around the graph. They can also be described as a sequence of edges that allows
one vertex to be reached from another vertex in a graph.

A graph is said to be `connected` if there is a path from
each vertex to every other vertex.

A graph is also said to be `complete` if there is an edge from each vertex to every other vertex

## Graph Representation

How do we represent a graph in the computer? Some of the most commonly used representations of graphs are the adjacency
matrix, adjacency list and dictionary.

## Starting with a simple directed graph

```python
G = (
    {1,2,3,4},
    {(1,2), (1,3), (1,4)},
)
```

The graph G has 4 vertices v and 3 edges e. It is represented pictorially as 4 labeled circles (vertices) with 3 lines (edges)

## Belman Ford

The Bellman-Ford algorithm is best suited to find the shortest paths in a directed graph, with one or more negative edge weights, from the source vertex to all other vertices.

It does so by repeatedly checking all the edges in the graph for shorter paths, as many times as there are vertices in the graph (minus 1).

## Problems

- Clone graph (LeetCode #45, Blind)
- Course Schedule (LeetCode #210, Blind)
- Pacific Atlantic Water Flow (LeetCode #417, Blind)
- Number of Islands (LeetCode #200, Blind)
- Longest Consecutive Subsequence (LeetCode #128, Blind)
- Alien Dictionary (LeetCode #269, Blind)
- Graph Valid tree (LeetCode #261, Blind)
- Number of connected components in an undirected graph (LeetCode #323, Blind)
