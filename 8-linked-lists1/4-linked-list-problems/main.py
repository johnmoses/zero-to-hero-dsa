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

def merge_k_lists(lists):
    nodes = []
    head = point = Node(0)
    for ln in lists:
        while ln:
            nodes.append(ln.val)
            ln = ln.next
    for x in sorted(nodes):
        point.next = Node(x)
        point = point.next
    return head.next

print(merge_k_lists([Node([1,4,5]), Node([1,3,4]), Node([2,6])]))