# Linked Lists Introduction - Python Example

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating linked list with two nodes
node1 = Node(1)
node2 = Node(2)
node1.next = node2

# Traversing linked list
current = node1
while current:
    print(current.data)
    current = current.next
