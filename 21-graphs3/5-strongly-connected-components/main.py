# Strongly Connected Components - Kosaraju's Algorithm - Python Example

from collections import defaultdict

def dfs(graph, v, visited, stack=None):
    visited.add(v)
    for nbr in graph[v]:
        if nbr not in visited:
            dfs(graph, nbr, visited, stack)
    if stack is not None:
        stack.append(v)

def reverse_graph(graph):
    rev = defaultdict(list)
    for u in graph:
        for v in graph[u]:
            rev[v].append(u)
    return rev

def kosaraju_scc(graph):
    visited = set()
    stack = []

    for vertex in graph:
        if vertex not in visited:
            dfs(graph, vertex, visited, stack)

    rev = reverse_graph(graph)
    visited.clear()
    sccs = []

    while stack:
        v = stack.pop()
        if v not in visited:
            comp = []
            dfs(rev, v, visited, comp)
            sccs.append(comp)

    return sccs

graph = {
    0: [1],
    1: [2],
    2: [0, 3],
    3: [4],
    4: []
}

components = kosaraju_scc(graph)
print("Strongly connected components:", components)
