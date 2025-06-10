"""
Merge K Lists
"""

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        self.nodes = []
        head = point = ListNode(0)
        for i in lists:
            while i:
                self.nodes.append(i.val)
                i = i.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next

lists = [[1,4,5],[1,3,4],[2,6]]
sn = Solution()
print(sn.mergeKLists(lists))