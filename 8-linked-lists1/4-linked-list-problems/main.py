# Linked List Problems - Python Example

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_list(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

# Usage
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

reversed_head = reverse_list(head)
current = reversed_head
while current:
    print(current.data)
    current = current.next
