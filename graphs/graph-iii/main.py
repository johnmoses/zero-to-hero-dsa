""" 
Undirected adjacency matrix graph with more features
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

    def check_visited(self, v, visited):
        visited[v] = True
        print(self.nodes[v], end=' ')

        for i in range(self.size):
            if self.edges[v][i] == 1 and not visited[i]:
                self.check_visited(i, visited)

    def dfs(self, start_node):
        queue = self.nodes.index(start_node)
        visited = [False] * self.size
        self.check_visited(queue, visited)
    
    def bfs(self, start_node):
        queue = [self.nodes.index(start_node)]
        visited = [False] * self.size
        visited[queue[0]] = True
            
        while queue:
            current_node = queue.pop(0)
            print(self.nodes[current_node], end=' ')
        
            for i in range(self.size):
                if self.edges[current_node][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True

class Graph1:
    def __init__(self, size):
        self.size = size
        self.nodes = [''] * size
        self.edges = [[0] * size for _ in range(size)]

    def add_node(self, index, value):
        if 0 <= index < self.size:
            self.nodes[index] = value

    def add_edge(self, u, v):
        if 0 <= u < self.size:
            self.edges[u][v] = 1
            self.edges[v][u] = 1

    def print_graph(self):
        for row in self.edges:
            print(''.join(map(str, row)))
        for node, value in enumerate(self.nodes):
            print(f'Node {node} {value}')

    def check_visited(self, v, visited):
        visited[v] = True
        print(self.nodes[v], end=' ')
        for i in range(self.size):
            if self.edges[v][i] == 1 and not visited[i]:
                self.check_visited(i, visited)

    def dfs(self, start_node):
        queue = self.nodes.index(start_node)
        visited = [False] * self.size
        self.check_visited(queue, visited)

    def bfs(self, start_node):
        queue = [self.nodes.index(start_node)]
        visited = [False] * self.size
        visited[queue[0]] = True
        while queue:
            current_node = queue.pop(0)
            print(self.nodes[current_node], end=' ')
            for i in range(self.size):
                if self.edges[current_node] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True

g = Graph1(7)
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

start_node = 'A'
print(f"\nDepth First Search starting from {start_node}")
g.dfs(start_node)

print(f"\nBreadth First Search starting from {start_node}")
g.bfs(start_node)