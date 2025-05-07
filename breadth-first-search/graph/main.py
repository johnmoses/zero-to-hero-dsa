""" 
Breadth First Search by queue on a graph
Example 1:
    Input: graph = [[2,3,8],[1,7],[1,4,5],[2,6]]
    Output: [2,3,4,5,6,8,7]
"""
from collections import deque

def bfs(graph, start=1):
    # Initialize visited set and result list
    visited = set()
    result = []
    
    # Create queue and add start node 
    queue = deque([start])
    visited.add(start)
    
    # BFS traversal
    while queue:
        # Get next node from queue
        node = queue.popleft()
        result.append(node)
        
        # Add unvisited neighbors to queue
        for neighbor in graph[node-1]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return result

print(bfs([[2,3,8],[1,7],[1,4,5],[2,6]]))