"""
Reverse List
"""
head = [1,2,3,4,5]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev_node = None
        curr_node = head
        while curr_node:
            next_node = curr_node.next # Remember next node
            curr_node.next = prev_node  # REVERSE! None, first time round.
            prev_node = curr_node  # Used in the next iteration.
            curr_node = next_node  # Move to next node.
        head = prev_node
        return head

    # def __str__(self):
    #     values = [str(x.head) for x in self]
    #     return ' -> '.join(values)

sn = Solution()
print(sn.reverseList(ListNode(head)))