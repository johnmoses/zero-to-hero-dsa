# Connected Components - Python Example (Undirected graph)

def dfs(graph, node, visited):
    visited.add(node)
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def connected_components(graph):
    visited = set()
    components = []
    for node in graph.keys():
        if node not in visited:
            comp = []
            dfs_collect(graph, node, visited, comp)
            components.append(comp)
    return components

def dfs_collect(graph, node, visited, comp):
    visited.add(node)
    comp.append(node)
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs_collect(graph, neighbor, visited, comp)

graph = {
    0: [1],
    1: [0, 2],
    2: [11],
    3: []
}

print("Connected Components:", connected_components(graph))
