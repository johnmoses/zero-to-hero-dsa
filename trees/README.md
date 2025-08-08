# Trees

A tree T can be defined formally as a set of nodes storing elements such that the nodes have a parent-child relationship.

A tree is quite similar to linked list in that each node contains data and can be linked to other nodes. However it is different in the hierarichical non-linear structure.

If T is nonempty, it has a special node, called the root of T , that has no parent.
Each node v of T different from the root has a unique parent node w; every node with parent w is a child of w.

A tree is and abstract data type (ADT) that stores elements hierarchically. It is the most important non-linear data structure in computing. It has made better file systems, graphic user interfaces, database, web sites and lots more.

The relationship between objects are hierarichal in terms of parent-child, ancestor-decendants arrangements. It is typically like a tree that has a root, branches, and branches that have branches on and on.

Programatically we could define a tree T as a set of nodes storing elements such that the nodes have a parent-child relationship

A typical implementation of a tree is binary trees that use linked structures

## Tree Terminology

- Node: An item stored in the tree
- Root: The topmost node that has no parent
- Child: A node immediately below and directly connected to a given node
- Parent: A node immediately above and directly connected to a given node
- Siblings: The children of a common parent
- Leaf: A node that has no children
- Interior node: A node that has at least one child
- Edge/Branch/Link: The line that connects a parent to the child
- Descendant: All the node's children down to the leaves
- Ancestor: A node's parent up to the root
- Path: The sequence of edges that connects a node with one of its descendants
- Path Length: The number of edges in a path
- Depth or Level: The length of the path connecting the root
- Height: The length of the longest path
- Subtree: A tree formed from viewpoint of a node and all its descendants

## Applications of Tree Data Structure

- Hierarchical Data: File systems, organizational models, etc.
- Databases: Used for quick data retrieval.
- Routing Tables: Used for routing data in network algorithms.
- Sorting/Searching: Used for sorting data and searching for data.
- Priority Queues: Priority queue data structures are commonly implemented using trees, such as binary heaps.

## Types of Trees

### Binary Trees

Each node has up to two children, the left child node and the right child node. This structure is the foundation for more complex tree types like Binay Search Trees and AVL Trees.

### Binary Search Tree

A binary search tree (BST), a special form of a binary tree, satisfies the binary search property:

- The value in each node must be greater than (or equal to) any values stored in its left subtree.
- The value in each node must be less than (or equal to) any values stored in its right subtree.

One of the biggest advantages of Binary Search Trees is that operations like search, delete, and insert are fast and done without having to shift values in memory.

A binary tree can be traversed in preorder, inorder, postorder or level-order. Among these traversal methods, preorder, postorder and level-order traversal are suitable to be extended to an N-ary tree.

### AVL Tree

Invented by Adel' son- Vel'skii and Landis
The AVL Tree is a type of Binary Search Tree named after two Soviet inventors Georgy Adelson-Velsky and Evgenii Landis who invented the AVL Tree in 1962.

AVL trees are self-balancing, which means that the tree height is kept to a minimum so that a very fast runtime is guaranteed for searching, inserting and deleting nodes, with time complexity O(logn).

### Splay Trees

Splay tree is a self-adjusting binary search tree data structure, which means that the tree structure is adjusted dynamically based on the accessed or inserted elements. In other words, the tree automatically reorganizes itself so that frequently accessed or inserted elements become closer to the root node.

### Red-black Trees

Red Black Trees are a type of balanced binary search tree that use a set of rules to maintain balance, ensuring logarithmic time complexity for operations like insertion, deletion, and searching, regardless of the initial shape of the tree. Red Black Trees are self-balancing, using a simple color-coding scheme to adjust the tree after each modification

### N-ary tree

A binary tree is a rooted tree in which each node has no more than 2 children. Let's extend this definition to N-ary tree. If a tree is a rooted tree in which each node has no more than N children, it is called N-ary tree. Trie is one of the most frequently used N-ary trees.

### Tries

A Trie or prefix tree is a special form of a N-ary tree. Typically, a trie is used to store strings. Each Trie node represents a string (a prefix). Each node might have several children nodes while the paths to different children nodes represent different characters. And the strings the child nodes represent will be the origin string represented by the node itself plus the character on the path

### Heaps

A Heap is a complete binary tree data structure that satisfies the heap property: for every node, the value of its children is greater than or equal to its own value. Heaps are usually used to implement priority queues, where the smallest (or largest) element is always at the root of the tree

## Problems

- Validate Binary Search Tree (LeetCode # 98, Blind)
- Same Tree (LeetCode # 100, Blind)
- Binary tree level order traversal (LeetCode # 102, Blind, Grind)

- Maximun depth of binary tree (LeetCode # 104, Blind)
- Construct Binary Tree from Preorder and Inorder Traversal (LeetCode # 105, Blind)
- Binary tree maximum path sum (LeetCode # 124, Blind)
- Implement Trie (Prefix Tree) (LeetCode # 208, Blind)
- Add and search word (LeetCode # 211, Blind)
- Word Search II (LeetCode # 212, Blind)
- Kth Largest Element in an Array (LeetCode #215)
- Invert/Flip Binary Tree (LeetCode # 226, Blind)
- Kth Smallest Element in a BST (LeetCode # 230, Blind)
- Lowest Common Ancestor of a Binary Search Tree (LeetCode # 235, Blind)
- Serialize and Deserialize Binary Tree (LeetCode # 297, Blind)
- Top K Frequent Elements (LeetCode #347)
- Find K Pairs with Smallest Sums (LeetCode #373)
- Subtree of another tree (LeetCode # 572, Blind)
