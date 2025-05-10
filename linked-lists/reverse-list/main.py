"""
Reverse List
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
    dummy_node = ListNode()

    # Start from head node
    current_node = head

    # Iterate over the list
    while current_node is not None:
        # Store next node
        next_node = current_node.next

        # Reverse the link so that current_node.next points to the node before it
        current_node.next = dummy_node.next
        dummy_node.next = current_node

        # Move to the next node in the original list
        current_node = next_node
    # Return dummy node's next which now points to the head of the reversed list
    curr = dummy_node.next
    while curr:
        print(curr.val)
        curr = curr.next
    return dummy_node.next

reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
