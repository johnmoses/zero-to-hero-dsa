""" 
Undirected Graph with cyclic detection
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

    def check_visited(self, v, visited, parent):
        visited[v] = True

        for i in range(self.size):
            if self.edges[v][i] == 1:
                if not visited[i]:
                    if self.check_visited(i, visited, v):
                        return True
                elif parent != i:
                    return True
        return False


    def is_cyclic(self):
        visited = [False] * self.size
        for i in range(self.size):
            if not visited[i]:
                if self.check_visited(i, visited, -1):
                    return True
        return False

g = Graph(4)
g.add_node(0, 'A')
g.add_node(1, 'B')
g.add_node(2, 'C')
g.add_node(3, 'D')
g.add_edge(0, 1)  # A - B
g.add_edge(0, 2)  # A - C
g.add_edge(0, 3)  # A - D
g.add_edge(1, 2)  # B - C

g.print_graph()

print("\nGraph has cycle:", g.is_cyclic())