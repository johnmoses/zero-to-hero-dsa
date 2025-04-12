""" 
Find lowest value in the linked list
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_lowest_value(head):
    min_value = head.data
    current_node = head.next
    while current_node:
        if current_node.data < min_value:
            min_value = current_node.data
        current_node = current_node.next
    return min_value

a = Node(20)
b = Node(30)
c = Node(40)
d = Node(10)
e = Node(70)

a.next = b
b.next = c
c.next = d
d.next = e

print(find_lowest_value(a))