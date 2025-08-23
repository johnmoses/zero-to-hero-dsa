# Cycle Detection in Linked Lists

## Introduction
Cycle detection identifies whether a linked list contains a loop, where a node’s next pointer points back to a previous node.

## Details
The fast and slow pointers technique (Floyd’s Tortoise and Hare) detects cycles by moving pointers at different speeds and checking for meeting points.

Detecting cycles prevents infinite loops and is essential in various applications.

## Examples
If fast and slow pointers meet, a cycle exists.

## Key Concepts
- Use two pointers moving at different speeds.  
- Meeting point indicates a cycle.  
- Detection in O(n) time and O(1) space.

## Summary
Cycle detection is fundamental for safe traversal of linked lists and related data structures.
