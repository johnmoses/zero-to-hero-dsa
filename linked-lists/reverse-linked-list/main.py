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
    # Initialize previous node as None
    prev = None

    # Start from head node
    current = head

    # Iterate over the list
    while current is not None:
        # Store next node
        next_node = current.next

        # Reverse the link so that current_node.next points to the node before it
        current.next = prev
        # Move prev to current node
        prev = current
        # Move current to next node
        current = next_node

    # Print the reversed list
    while prev:
        print(prev.val, end=' -> ')
        prev = prev.next
    # Return output
    return prev


reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))