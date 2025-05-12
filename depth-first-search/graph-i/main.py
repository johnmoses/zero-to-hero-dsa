""" 
Depth-first-search traversal
"""
class Graph:
    def __init__(self, size):
        self.size = size
        self.edges = [[0] * size for _ in range(size)]
        self.nodes = [''] * size  

    # Edges in the matrix
    def add_edge(self, u, v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.edges[u][v] = 1
            self.edges[v][u] = 1

    # Nodes or vertices
    def add_node(self, node, data):
        if 0 <= node < self.size:
            self.nodes[node] = data

    def print_graph(self):
        print("\nEdges:")
        for row in self.edges:
            print(' '.join(map(str, row)))
        print("\nNodes:")
        for node, data in enumerate(self.nodes):
            print(f"Node {node}: {data}")

    def check_visited(self, v, visited):
        visited[v] = True
        print(self.nodes[v], end=' ')

        for i in range(self.size):
            if self.edges[v][i] == 1 and not visited[i]:
                self.check_visited(i, visited)

    def dfs(self, node_data):
        visited = [False] * self.size
        start_node = self.nodes.index(node_data)
        self.check_visited(start_node, visited)

g = Graph(4)
g.add_node(0, 'A')
g.add_node(1, 'B')
g.add_node(2, 'C')
g.add_node(3, 'D')
g.add_node(4, 'E')
g.add_node(5, 'F')
g.add_node(6, 'G')
g.add_edge(3, 0)  # D - A
g.add_edge(0, 2)  # A - C
g.add_edge(0, 3)  # A - D
g.add_edge(0, 4)  # A - E
g.add_edge(4, 2)  # E - C
g.add_edge(2, 5)  # C - F
g.add_edge(2, 1)  # C - B
g.add_edge(2, 6)  # C - G
g.add_edge(1, 5)  # B - F

g.print_graph()

start_node = 'D'
print(f"\nDepth First Search starting from {start_node}")
g.dfs(start_node)