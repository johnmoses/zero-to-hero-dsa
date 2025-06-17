""" 
Prim's Algorithm

This is a greedy algorithm used to find the minimum spanning tree (MST) for a weighted, undirected graph. 

Here's how it works: 
    
Initialization: 
Start with an arbitrary vertex in the graph and mark it as part of the MST. 
Create a set of visited vertices and a priority queue of edges.

Iteration:
Find all edges connecting the current MST to vertices not yet in the MST. 
Add these edges to the priority queue, sorted by weight.
Select the edge with the minimum weight from the priority queue. 
Add the new vertex connected by this edge to the MST. 

Termination: 
Repeat step 2 until all vertices are included in the MST.
"""
import heapq

def prim_mst(graph):
    start_node = 0
    visited = {start_node}
    pq = []
    
    for neighbor, weight in graph[start_node]:
        heapq.heappush(pq, (weight, start_node, neighbor))
    
    mst = []
    while pq:
        weight, u, v = heapq.heappop(pq)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            for neighbor, weight in graph[v]:
                if neighbor not in visited:
                    heapq.heappush(pq,(weight, v, neighbor))
    return mst

# Example graph represented as an adjacency list
graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8), (4, 9)],
    4: [(1, 5), (2, 7), (3, 9)]
}

mst = prim_mst(graph)
for edge in mst:
    print(f"{edge[0]} - {edge[1]}: {edge[2]}")
