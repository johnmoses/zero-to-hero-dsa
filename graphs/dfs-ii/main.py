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
search_value = "C"

def dfs(graph, start, search_value, visited = None):
    if visited is None:
        visited = set()
    
    if start == search_value:
        return True
    visited.add(start)

    for neighbour in graph[start]:
        if neighbour not in visited:
            found = dfs(graph, neighbour, search_value, visited)
            if found:
                return True
    return False
   
res = dfs(graph, start, search_value)
print(f"element {search_value} : {res}")