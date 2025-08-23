# Topological Sorting - Python Example (DFS based)

def topological_sort_util(v, adj, visited, stack):
    visited[v] = True
    for neighbor in adj[v]:
        if not visited[neighbor]:
            topological_sort_util(neighbor, adj, visited, stack)
    stack.append(v)

def construct_adj(V, edges):
    adj = [[] for _ in range(V)]
    for u, v in edges:
        adj[u].append(v)
    return adj

def topological_sort(V, edges):
    adj = construct_adj(V, edges)
    visited = [False] * V
    stack = []
    for i in range(V):
        if not visited[i]:
            topological_sort_util(i, adj, visited, stack)
    return stack[::-1]

V = 6
edges = [(2,3), (3,1), (4,0), (4,1), (5,0), (5,2)]

result = topological_sort(V, edges)
print("Topological sort order:", result)
