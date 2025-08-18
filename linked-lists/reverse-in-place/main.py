""" 
Reverse a sublist of a linked list from position m to n.

Example:
Input: head = [1, 2, 3, 4, 5], m = 2, n = 4
Output: [1, 4, 3, 2, 5]

Explanation:
Identify the start and end of the sublist.
Reverse the nodes in place by adjusting the pointers.
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_sublist(head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
    if m == n:
        return head

    # Create a dummy node to simplify the edge cases
    dummy_node = ListNode(0)
    dummy_node.next = head

    # Move the prev pointer to the node before the m position
    prev_node = dummy_node

    # Reverse th sublist from m to n positions
    for _ in range(m - 1):
        prev_node = prev_node.next

    # Reverse the sublist between m and n positions
    cur_node = prev_node.next
    nxt_node = cur_node.next

    for _ in range(n - m):
        cur_node.next = nxt_node.next
        nxt_node.next = prev_node.next
        prev_node.next = nxt_node
        nxt_node = cur_node.next
    
    # Print list
    current = dummy_node
    while current:
        print(current.val, end=' -> ')
        current = current.next

    return dummy_node.next

reverse_sublist(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2, 4)