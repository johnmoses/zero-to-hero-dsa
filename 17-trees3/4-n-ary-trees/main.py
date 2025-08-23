# N-ary Tree Implementation and Level-Order Traversal - Python Example

class NaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def level_order(root):
    if not root:
        return
    from collections import deque
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.data, end=" ")
        for child in node.children:
            queue.append(child)

# Example usage
root = NaryTreeNode(1)
child1 = NaryTreeNode(2)
child2 = NaryTreeNode(3)
child3 = NaryTreeNode(4)

root.children = [child1, child2, child3]
child1.children = [NaryTreeNode(5), NaryTreeNode(6)]

print("Level order traversal of N-ary tree:")
level_order(root)
