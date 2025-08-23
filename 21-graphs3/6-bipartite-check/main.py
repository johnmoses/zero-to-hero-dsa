# Bipartite Graph Check using BFS - Python Example

from collections import deque

def is_bipartite(graph):
    color = {}
    for node in graph:
        if node not in color:
            queue = deque([node])
            color[node] = 0

            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if v not in color:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        return False
    return True

graph1 = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2]
}

graph2 = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1]
}

print("Graph1 is bipartite:", is_bipartite(graph1))  # True
print("Graph2 is bipartite:", is_bipartite(graph2))  # False
