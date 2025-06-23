"""
Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    # Initialize a dummy node, which will be the new head after reversal
    prev = ListNode()

    # Start from head node
    curr = head

    # Iterate over the list
    while curr is not None:
        print(curr.val)
        # Store next node
        next_node = curr.next

        # Reverse the link so that current_node.next points to the node before it
        curr.next = prev.next
        prev.next = curr

        # Move to the next node in the original list
        curr = next_node
    # Return output
    return prev.next

def reverseList1(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        print(prev)
    return prev

reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
reverseList1(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
