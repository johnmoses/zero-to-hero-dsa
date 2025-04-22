"""
Singly Linked Lists

Given some nodes with values 20, 30, 40, design a fully functional singly linked list with the following operations:
    - get value of node
    - add node at head
    - add node at tail
    - add node at index
    - delete node at index
    - traverse and display nodes
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def get_value(self, index):
        if self.head is None:
            return None
        current = self.head
        for i in range(index):
            if current is None:
                return None
            current = current.next
        return current.value if current else None

        
    def add_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

        
    def add_tail(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node


    def add_at_index(self, value, index):
        if index == 0:
            self.add_head(value)
            return
        new_node = Node(value)
        current = self.head
        for i in range(index-1):
            if current is None:
                return
            current = current.next
        if current is None:
            return

        new_node.next = current.next
        current.next = new_node

        
    def delete_at_index(self, index):
        if self.head is None:
            return
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        for i in range(index-1):
            if current is None:
                return
            current = current.next

        if current is None or current.next is None:
            return
        current.next = current.next.next

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
        print("")

    def __str__(self):
        values = [str(x.value) for x in self]
        return ' -> '.join(values)

ll = LinkedList()
ll.add_head(20)
ll.add_head(30)
ll.add_tail(40)
print(ll.get_value(0))
print(ll.get_value(1))
ll.display()
ll.delete_at_index(2)
ll.display()
# print(ll)