"""
Middle of the Linked List (LeetCode 876)
Given a non-empty, singly linked list with head node head, return a middle node of the linked list.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def middle_node(head: ListNode) -> ListNode:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# Example for Middle of the Linked List
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
middle = middle_node(head)
print("The middle node of the linked list is:", middle.val)
