""" 
Adjacency list graph with OOP approach
"""

class Node:
    def __init__(self, data):
        self.data = data    # Stored data
        self.next = None    # Next pointer

class Graph:
    def __init__(self, size):
        self.size = size
        self.nodes = [None] * self.size

    # Add edges
    def add_edge(self, s, d):
        node = Node(d)
        node.next = self.nodes[s]
        self.nodes[s] = node

        node = Node(s)
        node.next = self.nodes[d]
        self.nodes[d] = node

    # Print the graph
    def print_graph(self):
        for i in range(self.size):
            print("Node " + str(i) + ":", end="")
            temp = self.nodes[i]
            while temp:
                print(" -> {}".format(temp.data), end="")
                temp = temp.next
            print(" \n")

g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(1, 2)

g.print_graph()