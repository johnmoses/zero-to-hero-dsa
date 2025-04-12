""" 
Adjacency list graph
"""

def add_edge(adj, i, j):
    adj[i].append(j)
    adj[j].append(i)  # Undirected

def display_adj_list(adj):
    for i in range(len(adj)):
        print(f"{i}: ", end="")
        for j in adj[i]:
            print(j, end=" ")
        print()

# Create a graph with specified size or nodes and no edges
adj = [[] for _ in range(5)]

# Add edges one by one
add_edge(adj, 0, 1)
add_edge(adj, 0, 2)
add_edge(adj, 1, 2)
add_edge(adj, 2, 3)

print("Adjacency List Graph:")
display_adj_list(adj)