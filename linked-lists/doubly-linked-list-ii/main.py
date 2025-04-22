"""
Doubly-Linked List
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)

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

    def add(self, value):
        if self.head is None:
            node = Node(value)
            self.head = node
            self.tail = node
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

ll = LinkedList()
ll.add(20)
ll.add(30)
ll.add(40)

print(ll)
print(len(ll))
