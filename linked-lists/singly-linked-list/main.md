# Singly-linked Lists

This is a linear data structure where each element (node) contains data and a reference (pointer) to the next node in the sequence. Unlike arrays, linked lists do not store elements in contiguous memory locations. This structure allows for efficient insertion and deletion of elements without the need to shift other elements.

## Key Characteristics

Nodes: Each element in a linked list is a node, consisting of two parts:

Data: The value or information stored in the node.

Next Pointer: A reference to the next node in the sequence. The last node's pointer is typically set to None.

Head: The first node in the list, acting as the entry point for traversal.

Traversal: Linked lists can only be traversed sequentially, starting from the head and following the next pointers.

## Basic Operations

Insertion:
At the Beginning: Create a new node, set its next pointer to the current head, and update the head to point to the new node.
At the End: Traverse to the last node, set its next pointer to the new node.

- At a Specific Index: Traverse to the node before the desired index, update pointers to insert the new node in between.

Deletion:

- At the Beginning: Update the head to point to the second node.
- At the End: Traverse to the second-to-last node, update its next pointer to None.
- At a Specific Index: Traverse to the node before the desired index, update pointers to remove the node at the specified index.

Search:
Traverse the list, comparing each node's data with the target value until found or the end is reached.
