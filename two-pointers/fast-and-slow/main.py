""" 
Detect if a linked list has a cycle.

Example 1:
Input: head = [1,2], pos = 0
Output: true

Example 2
Input: head = [1], pos = -1
Output: false

Explanation:
Initialize two pointers, one moving one step at a time (slow) and the other moving two steps at a time (fast).
If there is a cycle, the fast pointer will eventually meet the slow pointer.
If the fast pointer reaches the end of the list, there is no cycle.
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def has_cycle(head):
    """
    Returns True if linked list has a cycle, False otherwise
    Uses Floyd's cycle detection algorithm (fast/slow pointers)
    """
    if not head or not head.next:
        return False
        
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next  
        fast = fast.next.next
        if slow == fast:
            return True
            
    return False

def has_cycle1(head: ListNode) -> bool:
    if not head or not head.next:
            return False
        
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next  
        fast = fast.next.next
        if slow == fast:
            return True
            
    return False

# print(has_cycle(ListNode(1)))
# print(has_cycle1(ListNode(1)))
# print(has_cycle(ListNode([1,2])))
print(has_cycle1(ListNode([1,2])))
