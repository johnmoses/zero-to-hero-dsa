""" 
Directed and weighted adjacency matrix graph
"""
class Graph:
    def __init__(self, size):
        self.size = size
        self.nodes = [''] * size  
        self.edges = [[0] * size for _ in range(size)]

    # Nodes or vertices
    def add_node(self, index, value):
        if 0 <= index < self.size:
            self.nodes[index] = value

    # Edges in the matrix
    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.edges[u][v] = weight
            self.edges[v][u] = weight

    def print_graph(self):
        print("\nEdges:")
        for row in self.edges:
            print(' '.join(map(str, row)))
        print("\nNodes:")
        for node, value in enumerate(self.nodes):
            print(f"Node {node}: {value}")

g = Graph(4)
g.add_node(0, 'A')
g.add_node(1, 'B')
g.add_node(2, 'C')
g.add_node(3, 'D')
g.add_edge(0, 1, 3)  # A -> B with weight 3
g.add_edge(0, 2, 2)  # A -> C with weight 2
g.add_edge(3, 0, 4)  # D -> A with weight 4
g.add_edge(2, 1, 1)  # C -> B with weight 1

g.print_graph()