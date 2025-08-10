""" 
A simple Graph implementation with basic functionalities using both adjacency list and matrix representations
"""
class Node:
    def __init__(self, value):
        """Initialize a node with a value"""
        self.value = value
    
    def __str__(self):
        """String representation of the node"""
        return str(self.value)
    
    def __repr__(self):
        """Representation of the node"""
        return str(self.value)

class Graph:
    def __init__(self, directed=False):
        """
        Initialize a graph object.
        Args:
            directed: True for directed graph, False for undirected
        """
        self.graph = {}  # Adjacency list
        self.directed = directed
    
    def add_node(self, value) -> Node:
        """Create and add a new node to the graph"""
        new_node = Node(value)
        if new_node.value not in self.graph:
            self.graph[new_node.value] = []
        return new_node
    
    def add_edge(self, from_node, to_node) -> None:
        """Add an edge between two nodes"""
        # Add nodes if they don't exist
        if from_node.value not in self.graph:
            self.graph[from_node.value] = []
        if to_node.value not in self.graph:
            self.graph[to_node.value] = []
        
        # Add the edge
        self.graph[from_node.value].append(to_node.value)
        
        # If undirected, add reverse edge
        if not self.directed:
            self.graph[to_node.value].append(from_node.value)
    
    def remove_edge(self, from_node, to_node) -> None:
        """Remove an edge between two nodes"""
        if from_node.value in self.graph and to_node.value in self.graph:
            if to_node.value in self.graph[from_node.value]:
                self.graph[from_node.value].remove(to_node.value)
            
            if not self.directed:
                if from_node.value in self.graph[to_node.value]:
                    self.graph[to_node.value].remove(from_node.value)
    
    def get_neighbors(self, node) -> list:
        """Get all neighbors of a node"""
        return [Node(val) for val in self.graph.get(node.value, [])]
    
    def bfs(self, start_node) -> list:
        """
        Perform Breadth-First Search starting from start_node
        Returns list of node values in BFS order
        """
        if start_node.value not in self.graph:
            return []
        
        visited = set()
        queue = [start_node.value]
        result = []
        
        while queue:
            node_value = queue.pop(0)
            if node_value not in visited:
                visited.add(node_value)
                result.append(node_value)
                queue.extend(val for val in self.graph[node_value] 
                           if val not in visited)
        
        return [Node(val) for val in result]
    
    def dfs(self, start_node) -> list:
        """
        Perform Depth-First Search starting from start_node
        Returns list of node values in DFS order
        """
        if start_node.value not in self.graph:
            return []
        
        visited = set()
        result = []
        
        def dfs_recursive(node_value):
            visited.add(node_value)
            result.append(node_value)
            for neighbor in self.graph[node_value]:
                if neighbor not in visited:
                    dfs_recursive(neighbor)
        
        dfs_recursive(start_node.value)
        return [Node(val) for val in result]
    
    def has_path(self, start_node, end_node) -> bool:
        """Check if there's a path between start_node and end_node"""
        if (start_node.value not in self.graph or 
            end_node.value not in self.graph):
            return False
        
        visited = set()
        
        def dfs_path(current_value):
            if current_value == end_node.value:
                return True
            
            visited.add(current_value)
            for neighbor in self.graph[current_value]:
                if neighbor not in visited and dfs_path(neighbor):
                    return True
            return False
        
        return dfs_path(start_node.value)
    
    def print_graph(self) -> None:
        """Print the graph structure"""
        for node_value in self.graph:
            print(f"Node {node_value} -> {self.graph[node_value]}")

# Undirected graph
g = Graph(directed=False)

# Nodes
node1 = g.add_node(Node('A'))
node2 = g.add_node(Node('B'))
node3 = g.add_node(Node('C'))
node4 = g.add_node(Node('D'))
node5 = g.add_node(Node('E'))

# Edges
edges = [
    (node1, node2),  # A - B
    (node1, node3),  # A - C
    (node2, node4),  # B - C
    (node2, node5),  # B - E),
    (node3, node5),   # C - E
    (node4, node5)
]

for from_node, to_node in edges:
    g.add_edge(from_node, to_node)

print("Graph Structure:")
g.print_graph()

print("DFS Traversal from A:", g.dfs(Node('A')))  # ['A', 'B', 'C', 'D']")
print("BFS Traversal from A:", g.bfs(Node('A')))  # ['A', 'B', 'C', 'D']

print("\nPath from A to C:", g.has_path(Node('A'), Node('C')))  # True
print("Path from A to E:", g.has_path(Node('A'), Node('E')))  # False

# Directed graph
dg = Graph(directed=True)

# Nodes
node1 = dg.add_node(1)
node2 = dg.add_node(2)
node3 = dg.add_node(3)
node4 = dg.add_node(4)
node5 = dg.add_node(5)

# Add directed edges
directed_edges = [
    (node1, node2), (node2, node3),
    (node3, node4), (node4, node2),
    (node2, node5)
]

for from_node, to_node in directed_edges:
    dg.add_edge(from_node, to_node)

print("\nDirected graph structure:")
dg.print_graph()
print("\nDFS Traversal from Node 1:", dg.dfs(node1))  # [1, 2, 3, 4, 5]
print("Path from Node 1 to Node 5:", dg.has_path(node1, node5))  # True
