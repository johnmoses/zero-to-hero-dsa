""" 
Binary Tree from dictionary
"""
dct = [15, 10, 8, 12, 20, 16, 25] 

class Node:
    def __init__(self, values, left= None, right = None):
        self.values = values
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.values)

def build_tree(values):
    
    # Check if we have values; if we don't then return None
    if not values:
        return None

    # Create our tree object from the root and then
    # add it to a list of nodes that we can add values to
    tree = Node(values[0])
    queue = [values[0]]    

    # Iterate over the rest of the nodes and add
    # them to the tree
    index = 0
    for i in range(1, len(values) - 1):

        # If our node is None then we have a leaf so
        # there's no work to do; otherwise, create the
        # node and add it to the proper spot
        if values[i] is not None:

            # Create the node from the data
            node = Node(values[i])

            # If the index we're looking at is even
            # then we have a left branch; otherwise we
            # have a right branch so add the node to the
            # appropriate side of the tree
            if i % 2 == 0:
                queue[index] = node
            else:
                queue[index] = node

            # Add the node to our queue so it can
            # be referenced later
            queue.append(node)

        # Finally, update our index if we've finished looking
        # at this node. As each branch may only have two children
        # we only need to do this if we're looking at odd-indexed
        # entries because leaves will always be None (unless we've
        # reached the last level of the tree)
        index += i % 2

    return tree

print(build_tree(dct))