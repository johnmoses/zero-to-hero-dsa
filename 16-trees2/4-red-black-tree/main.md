# Red-Black Trees

## Introduction
Red-Black Trees are self-balancing binary search trees with additional color properties to maintain approximate balance and ensure O(log n) operations.

## Details
Each node is colored red or black with rules that guarantee tree height is logarithmic:

- The root is black.  
- Red nodes cannot have red children.  
- Black path property: every path from root to leaf has same number of black nodes.

Insertion and deletion include color changes and rotations to maintain properties.

## Examples
After inserting a node, recoloring and rotations restore red-black properties.

## Key Concepts
- Node colors enforce balance.  
- Rotations fix violations.  
- Ensures balanced tree height.

## Summary
Red-black trees offer efficient, balanced BST operations with less strict balancing than AVL trees.
