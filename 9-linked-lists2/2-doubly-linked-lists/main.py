# Doubly Linked List - Python Example

class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = DNode(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def print_forward(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
        print()

    def print_backward(self):
        curr = self.head
        if not curr:
            return
        while curr.next:
            curr = curr.next
        while curr:
            print(curr.data, end=" ")
            curr = curr.prev
        print()

dll = DoublyLinkedList()
dll.insert_at_head(3)
dll.insert_at_head(2)
dll.insert_at_head(1)

dll.print_forward()
dll.print_backward()
