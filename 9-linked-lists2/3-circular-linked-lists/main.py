# Circular Linked List - Python Example

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
            new_node.next = self.head

    def print_list(self):
        if not self.head:
            return
        curr = self.head
        while True:
            print(curr.data, end=" ")
            curr = curr.next
            if curr == self.head:
                break
        print()

cll = CircularLinkedList()
cll.append(1)
cll.append(2)
cll.append(3)
cll.print_list()
