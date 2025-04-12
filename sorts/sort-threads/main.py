""" 
Sort messages threads from server in chronological order

Input = [['root',1], [2,3], [3,0]]
Output = [0, 1, 2, 3]
"""
def sortThreads1(messages):
    """Sort message threads chronologically by walking through child-parent links"""
    # Build adjacency map 
    adjacency = {}
    for parent, child in messages:
        adjacency[child] = parent

    # Find root node
    root = None 
    for parent, child in messages:
        if parent not in adjacency:
            root = parent
            break

    # Walk graph and store order
    sorted_msgs = []
    def walk_thread(node):
        sorted_msgs.append(node)
        for parent, child in messages:
            if parent == node:
                walk_thread(child)

    walk_thread(root)
    return sorted_msgs

def sortThreads2(messages):
    res = []
    for i in messages:
        for j in i:
            if j == 'root':
                res.append(i[1])

    return res

print(sortThreads1([['root',1], [2,3], [3,0]]))
# print(sortThreads2([['root', 1], [2, 3], [3, 0]]))