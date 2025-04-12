"""
Given a list, rotate the list to the right by k places,
where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""

head = [1,2,3,4,5]
k = 1

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def rotate(head, k):
    # Check if head
    if not head or not head.next:
        return head
    current = head
    length = 1
    while current.next:
        current = current.next
        length += 1
    current.next = head
    k = k% length

    for i in range(length - k):
        current = current.next
    head = current.next
    current.next = None
    return head

print(rotate(ListNode(head), k))