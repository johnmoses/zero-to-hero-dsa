"""
Given a list, rotate the list to the right by k places,
where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next: Optional['ListNode']=None):
        self.val = val
        self.next = next

def rotate(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head or not head.next or k == 0:
        return head

    # Compute length and get last node
    current = head
    length = 1
    while current.next:
        current = current.next
        length += 1

    # Connect last node to head to make it circular
    current.next = head

    # Find the new tail: (length - k % length) steps
    k = k % length
    steps_to_new_tail = length - k
    new_tail = head
    for _ in range(steps_to_new_tail - 1):
        new_tail = new_tail.next

    # New head is next of new_tail
    new_head = new_tail.next
    new_tail.next = None

    # Print rotated list
    temp = new_head
    while temp:
        print(temp.val, end=' -> ')
        temp = temp.next
    print("NULL")

    return new_head

# Example usage:
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
rotate(head, 2)
