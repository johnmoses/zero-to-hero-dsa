"""
Merge two sorted linked lists and return it as a new list. The new list should
be made by splicing together the nodes of the first two lists.

For example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""
    
l1 = [1,2,4]
l2 = [1,3,4]

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

def merge_two_lists(l1, l2):
    """ 
    Merge lists recursively
    """
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.data < l2.data:
        l1.next = merge_two_lists(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_lists(l1, l2.next)
        return l2

print(merge_two_lists(Node(l1), Node(l2)))

def merge_two_lists_2(l1, l2):
    # Initialize result and current lists
    res = cur = Node(0)
    # Iterate over the two lists
    while l1 and l2:
        if l1.data < l2.data:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return res.next
    
print(merge_two_lists_2(Node(l1), Node(l2)))