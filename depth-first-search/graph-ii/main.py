""" 
Graph Depth-first-search traversal
"""
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
start = "E"
target = "C"

def dfs(graph, start, target, visited = None):
    if visited is None:
        visited = set()
    
    if start == target:
        return True
    visited.add(start)

    for i in graph[start]:
        if i not in visited:
            found = dfs(graph, i, target, visited)
            if found:
                return True
    return False
   
res = dfs(graph, start, target)
print(f"element {target} : {res}")