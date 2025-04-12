"""
Dijkistra Graph
Shortest path solution
"""

class Graph:
    def __init__(self, size):
        self.size = size
        self.nodes = [''] * size  
        self.edges = [[0] * size for _ in range(size)]

    # Nodes or vertices
    def add_node(self, index, data):
        if 0 <= index < self.size:
            self.nodes[index] = data

    # Edges in the matrix
    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.edges[u][v] = weight
            self.edges[v][u] = weight

    # Find shortest path from start node
    def dijkstra(self, data):
        node = self.nodes.index(data)
        distances = [float('inf')] * self.size
        distances[node] = 0
        visited = [False] * self.size

        for _ in range(self.size):
            min_distance = float('inf')
            u = None
            for i in range(self.size):
                if not visited[i] and distances[i] < min_distance:
                    min_distance = distances[i]
                    u = i

            if u is None:
                break

            visited[u] = True

            for v in range(self.size):
                if self.edges[u][v] != 0 and not visited[v]:
                    alt = distances[u] + self.edges[u][v]
                    if alt < distances[v]:
                        distances[v] = alt

        return distances

g = Graph(7)

g.add_node(0, 'A')
g.add_node(1, 'B')
g.add_node(2, 'C')
g.add_node(3, 'D')
g.add_node(4, 'E')
g.add_node(5, 'F')
g.add_node(6, 'G')

# Edges with weights (distances)
g.add_edge(3, 0, 4)  # D - A, weight 5
g.add_edge(3, 4, 2)  # D - E, weight 2
g.add_edge(0, 2, 3)  # A - C, weight 3
g.add_edge(0, 4, 4)  # A - E, weight 4
g.add_edge(4, 2, 4)  # E - C, weight 4
g.add_edge(4, 6, 5)  # E - G, weight 5
g.add_edge(2, 5, 5)  # C - F, weight 5
g.add_edge(2, 1, 2)  # C - B, weight 2
g.add_edge(1, 5, 2)  # B - F, weight 2
g.add_edge(6, 5, 5)  # G - F, weight 5

# Dijkstra's algorithm from selected node to all nodes
start_node = "B"
distances = g.dijkstra(start_node)
for i, d in enumerate(distances):
    print(f"Distance from {start_node} to {g.nodes[i]}: {d}")