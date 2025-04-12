# Trees

A tree T can be defined formally as a set of nodes storing elements such that the nodes have a parent-child relationship that satisfies the following properties

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
- Path: The sequence of edges that connects a noe with one of its descendants
- Path Length: The number of edges in a path
- Depth or Level: The length of the path connecting the root
- Height: The length of the longest path
- Subtree: A tree formed from viewpoint of a node and all its descendants

## Binary Search Tree

A binary tree can be traversed in preorder, inorder, postorder or level-order. Among these traversal methods, preorder, postorder and level-order traversal are suitable to be extended to an N-ary tree.

## AVL Tree

Invented by Adel' son- Vel'skii and Landis
The AVL Tree is a type of Binary Search Tree named after two Soviet inventors Georgy Adelson-Velsky and Evgenii Landis who invented the AVL Tree in 1962.

AVL trees are self-balancing, which means that the tree height is kept to a minimum so that a very fast runtime is guaranteed for searching, inserting and deleting nodes, with time complexity O(logn).

## Splay Trees

Splay tree is a self-adjusting binary search tree data structure, which means that the tree structure is adjusted dynamically based on the accessed or inserted elements. In other words, the tree automatically reorganizes itself so that frequently accessed or inserted elements become closer to the root node.

## Red-black Trees

Red Black Trees are a type of balanced binary search tree that use a set of rules to maintain balance, ensuring logarithmic time complexity for operations like insertion, deletion, and searching, regardless of the initial shape of the tree. Red Black Trees are self-balancing, using a simple color-coding scheme to adjust the tree after each modification

## N-ary tree

A binary tree is a rooted tree in which each node has no more than 2 children. Let's extend this definition to N-ary tree. If a tree is a rooted tree in which each node has no more than N children, it is called N-ary tree.

Trie is one of the most frequently used N-ary trees.

A Trie is a special form of a N-ary tree. Typically, a trie is used to store strings. Each Trie node represents a string (a prefix). Each node might have several children nodes while the paths to different children nodes represent different characters. And the strings the child nodes represent will be the origin string represented by the node itself plus the character on the path

In the example, the value we mark in each node is the string the node represents. For instance, we start from the root node and choose the second path 'b', then choose the first child 'a', and choose child 'd', finally we arrived at the node "bad". The value of the node is exactly formed by the letters in the path from the root to the node sequentially.

It is worth noting that the root node is associated with the empty string.

One important property of Trie is that all the descendants of a node have a common prefix of the string associated with that node. That's why Trie is also called prefix tree.

Let's look at the example again. For example, the strings represented by nodes in the subtree rooted at node "b" have a common prefix "b". And vice versa. The strings which have the common prefix "b" are all in the subtree rooted at node "b" while the strings with different prefixes will come to different branches.

Trie is widely used in various applications, such as autocomplete, spell checker, etc. We will introduce the practical applications in later chapters.

## Inserting a trie

When we insert a target value into a BST, in each node, we need to decide which child node to go according to the relationship between the value of the node and the target value. Similarly, when we insert a target value into a Trie, we will also decide which path to go depending on the target value we insert.

To be more specific, if we insert a string S into Trie, we start with the root node. We will choose a child or add a new child node depending on S[0], the first character in S. Then we go down to the second node and we will make a choice according to S[1]. Then we go down to the third node, so on and so for. Finally, we traverse all characters in S sequentially and reach the end. The end node will be the node which represents the string S.

## Searching

As we mentioned in the introduction to Trie, all the descendants of a node have a common prefix of the string associated with that node. Therefore, it should be easy to search if there are any words in the trie that starts with the given prefix.

Similarly, we can go down the tree depending on the given prefix. Once we can not find the child node we want, search fails. Otherwise, search succeeds.

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Constraints:

1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.

## Heaps

A Heap is a complete binary tree data structure that satisfies the heap property: for every node, the value of its children is greater than or equal to its own value. Heaps are usually used to implement priority queues, where the smallest (or largest) element is always at the root of the tree
