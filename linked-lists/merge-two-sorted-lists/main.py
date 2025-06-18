"""
Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

def mergeTwoLists(list1: Node, list2: Node) -> Node:
    head = Node()
    curr = head
    while list1 and list2:
        if list1.value < list2.value:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
    curr.next = list1 if list1 else list2
    return head.next

print(mergeTwoLists(Node([1,2,4]), Node([1,3,4])))