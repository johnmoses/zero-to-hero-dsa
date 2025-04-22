"""
Doubly-Linked List
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

# Instantiate Node
a = Node(20)
b = Node(30)
c = Node(40)

# Link the nodes
a.next = b
b.next = c

# Link the nodes backwards
b.prev = a
c.prev = b

# Traverse and display nodes forward in order
firstNode = a
while firstNode:
    print(firstNode.value, " ".join(" -> "))
    firstNode = firstNode.next

# Traverse and display nodes backward in order
lastNode = c
while lastNode:
    print(lastNode.value, " ".join(" -> "))
    lastNode = lastNode.prev