# Complex Linked List Manipulations - Python Example

class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def reverse_doubly_linked_list(head):
    current = head
    prev_node = None
    while current:
        prev_node = current.prev
        current.prev = current.next
        current.next = prev_node
        current = current.prev
    if prev_node:
        head = prev_node.prev
    return head

# Usage example
head = DNode(1)
node2 = DNode(2)
node3 = DNode(3)
head.next = node2
node2.prev = head
node2.next = node3
node3.prev = node2

head = reverse_doubly_linked_list(head)
curr = head
while curr:
    print(curr.data)
    curr = curr.next
