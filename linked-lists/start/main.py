"""
Singly Linked Lists

Given some nodes, 20, 30, 40, write a basic linked list to link the nodes, traverse and display the nodes in order.
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Create multiple instances of the node
a = Node(20)
b = Node(30)
c = Node(40)

# Link the nodes
a.next = b
b.next = c

# Traverse and display nodes in order

# Method 1
current = a # Set first node as current
while current:
    print(current.value, end=' -> ')
    # Set next pointer of current as new current node
    current = current.next
print()

# Method 2
current = a # Set first node as current
nodes = ""  # Variable to hold the values
while current:
    nodes += (str(current.value) + ' -> ')
    current = current.next
print(nodes)

# Method 3
current = a # Set first node as current
nodes = []  # Variable to hold the values
while current:
    nodes.append(current.value)
    current = current.next
values = [str(i) + ' -> ' for i in nodes]
print(values)
