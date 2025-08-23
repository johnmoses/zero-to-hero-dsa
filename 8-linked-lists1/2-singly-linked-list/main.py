# Singly Linked List - Python Example

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

# Usage
sll = SinglyLinkedList()
sll.insert_at_beginning(3)
sll.insert_at_beginning(2)
sll.insert_at_beginning(1)
sll.print_list()
