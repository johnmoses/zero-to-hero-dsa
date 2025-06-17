"""
Singly Linked Lists

Given some nodes with values 20, 30, 40, design a fully functional singly linked list
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

        
    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert_at_index(self, value, index):
        if index == 0:
            self.insert_at_beginning(value)
            return
        new_node = Node(value)
        current_node = self.head
        position = 0
        while current_node and position + 1 != index:
            position += 1
            current_node = current_node.next
        if current_node:
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not present")

    def delete_at_beginning(self):
        if self.head:
            self.head = self.head.next

    def delete_at_end(self):
        if not self.head or not self.head.next:
            self.head = None
            return
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
        current_node.next = None

    def delete_at_index(self, index):
        if index == 0:
            self.delete_at_beginning()
            return
        current_node = self.head
        position = 0
        while current_node and position + 1 != index:
            position += 1
            current_node = current_node.next
        if current_node and current_node.next:
            current_node.next = current_node.next.next
        else:
            print("Index not present")

    def search(self, target):
        current_node = self.head
        while current_node:
            if current_node.data == target:
                return True
            current_node = current_node.next
        return False

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
        print("")

    def __str__(self):
        current = self.head
        nodes = ''
        while current:
            nodes += (str(current.value))
        return nodes

ll = LinkedList()
ll.insert_at_beginning(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_end(40)
ll.insert_at_index(35, 3)
print(ll.get_value(0))
print(ll.get_value(1))
ll.display()
ll.delete_at_beginning()
ll.delete_at_end()
ll.delete_at_index(2)
ll.display()