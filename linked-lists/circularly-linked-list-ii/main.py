"""
Circularly-Linked List
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __str__(self):
        return ' -> '.join([str(item) for item in self])

    def __len__(self):
        return sum(1 for _ in self)

    def add(self, data):
        if self.head is None:
            newNode = Node(data)
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
        return self.tail

ll = LinkedList()
ll.add(1)
ll.add(2)

print(ll)
print(len(ll))
