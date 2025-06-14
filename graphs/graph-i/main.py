""" 
Undirected adjacency matrix graph
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
    def add_edge(self, u, v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.edges[u][v] = 1
            self.edges[v][u] = 1

    def print_graph(self):
        print("\nEdges:")
        for row in self.edges:
            print(' '.join(map(str, row)))
        print("\nNodes:")
        for node, value in enumerate(self.nodes):
            print(f"Node {node}: {value}")

g = Graph(5)
g.add_node(0, 'A')
g.add_node(1, 'B')
g.add_node(2, 'C')
g.add_node(3, 'D')
g.add_node(4, 'E')

g.add_edge(0, 1)  # A - B
g.add_edge(0, 2)  # A - C
g.add_edge(0, 3)  # A - D
g.add_edge(1, 2)  # B - C
g.add_edge(0, 4)  # A - E

g.print_graph()