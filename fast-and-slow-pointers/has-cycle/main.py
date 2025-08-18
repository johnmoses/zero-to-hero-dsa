"""
Linked List Cycle (LeetCode 141)
Given a linked list, determine if it has a cycle in it.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def has_cycle(head: ListNode) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Example for Linked List Cycle
head = ListNode(3)
node2 = ListNode(2)
node0 = ListNode(0)
node4 = ListNode(-4)
head.next = node2
node2.next = node0
node0.next = node4
node4.next = node2  # Cycle
print("Does the linked list have a cycle?", has_cycle(head))
