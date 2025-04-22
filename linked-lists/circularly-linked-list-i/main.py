"""
Circularly-Linked List
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Instantiate Node
a = Node(20)
b = Node(30)
c = Node(40)

# Link the nodes
a.next = b
b.next = c
c.next = a

# Traverse and display nodes in order
firstNode = a
startNode = a
print(firstNode.value, "".join(" -> "))
firstNode = firstNode.next

while firstNode != startNode:
    print(firstNode.value, " ".join(" -> "))
    firstNode = firstNode.next
