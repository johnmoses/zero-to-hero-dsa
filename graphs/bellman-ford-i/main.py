"""
Belman Ford Graph
Best Shortest path solutions
"""

class Graph:
    def __init__(self, size):
        self.size = size
        self.edges = [[0] * size for _ in range(size)]
        self.nodes = [''] * size  

    # Edges in the matrix
    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.edges[u][v] = weight
            # self.edges[v][u] = weight

    # Nodes or vertices
    def add_node(self, node, data):
        if 0 <= node < self.size:
            self.nodes[node] = data

    def bellman_ford(self, node_data):
        start_node = self.nodes.index(node_data)
        distances = [float('inf')] * self.size
        distances[start_node] = 0

        for i in range(self.size - 1):
            for u in range(self.size):
                for v in range(self.size):
                    if self.edges[u][v] != 0:
                        if distances[u] + self.edges[u][v] < distances[v]:
                            distances[v] = distances[u] + self.edges[u][v]
                            print(f"Relaxing edge {self.nodes[u]}-{self.nodes[v]}, Updated distance to {self.nodes[v]}: {distances[v]}")

        return distances

g = Graph(5)

g.add_node(0, 'A')
g.add_node(1, 'B')
g.add_node(2, 'C')
g.add_node(3, 'D')
g.add_node(4, 'E')

g.add_edge(3, 0, 4)  # D -> A, weight 4
g.add_edge(3, 2, 7)  # D -> C, weight 7
g.add_edge(3, 4, 3)  # D -> E, weight 3
g.add_edge(0, 2, 4)  # A -> C, weight 4
g.add_edge(2, 0, -3) # C -> A, weight -3
g.add_edge(0, 4, 5)  # A -> E, weight 5
g.add_edge(4, 2, 3)  # E -> C, weight 3
g.add_edge(1, 2, -4) # B -> C, weight -4
g.add_edge(4, 1, 2)  # E -> B, weight 2

# Running the Bellman-Ford algorithm from D to all vertices
print("\nThe Bellman-Ford Algorithm starting from vertex D:")
distances = g.bellman_ford('D')
for i, d in enumerate(distances):
    print(f"Distance from D to {g.nodes[i]}: {d}")