""" 
Traverse singly-linked list
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverse(head):
    node = head
    nodes = ''
    while node:
        nodes += (str(node.data) + ' -> ')
        node = node.next
    return nodes

a = Node(20)
b = Node(30)
c = Node(40)
d = Node(10)
e = Node(70)

a.next = b
b.next = c
c.next = d
d.next = e

print(traverse(a))