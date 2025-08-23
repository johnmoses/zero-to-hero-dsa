# Advanced Linked Lists Introduction - Python Example

class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class CDNode:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating doubly linked list
node1 = DNode(1)
node2 = DNode(2)
node1.next = node2
node2.prev = node1

# Creating circular linked list
node3 = CDNode(3)
node4 = CDNode(4)
node3.next = node4
node4.next = node3  # circular link
