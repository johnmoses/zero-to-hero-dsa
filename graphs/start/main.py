""" 
Graph Representation

 Given the nodes ['A', 'B', 'C', 'D', 'E'] and 
 edges = [
    [0, 1, 1, 1, 0],  # Edges for A
    [1, 0, 1, 0, 0],  # Edges for B
    [1, 1, 0, 0, 0],  # Edges for C
    [1, 0, 0, 0, 0],  # Edges for D
    [0, 1, 0, 0, 1]   # Edges for E
], Write a basic adjacency matrix graph representation in Python.
"""

nodes = ['A', 'B', 'C', 'D', 'E'] # Vertex or node data

edges = [
    [0, 1, 1, 1, 0],  # Edges for A
    [1, 0, 1, 0, 0],  # Edges for B
    [1, 1, 0, 0, 0],  # Edges for C
    [1, 0, 0, 0, 0],  # Edges for D
    [0, 1, 0, 0, 1]   # Edges for E
]

# Adjacency matrix
def print_edges(edges):
    print("\nEdges:")
    for row in edges:
        print(row)

def print_connections(edges, nodes):
    print("\nConnections:")
    for i in range(len(nodes)):
        print(f"{nodes[i]}: ", end="")
        for j in range(len(nodes)):
            if edges[i][j]:  # if there is a connection
                print(nodes[j], end=" ")
        print()  # new line

print('Nodes:',nodes)
print_edges(edges)
print_connections(edges, nodes)
