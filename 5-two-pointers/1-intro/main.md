# Introduction to Two Pointers

## Introduction
The two pointers technique uses two indices to traverse a data structure, often an array or string, to solve problems efficiently.

## Variants

- Left & Right Pointer (Approaching from both ends of Array)

- Slow & Fast Pointers: Using two pointers with different speed of movement. Typically they starts from the left end, then the first pointer advances fast and give some feedback to the slow pointer and do some calculation

## Details
Two pointers can move at different speeds or directions to find subarrays, pairs, or partitions. This technique reduces the need for nested loops, improving time complexity.

Applications include searching pairs with a sum, reversing arrays, and detecting cycles in linked lists.

## Examples
Using two pointers on a sorted array to find pairs summing to a target.

Example:
Input: nums = [1, 2, 3, 4, 6], target = 6
Output: [1, 3]

Explanation:
Initialize two pointers, one at the start (left) and one at the end (right) of the array.
Check the sum of the elements at the two pointers.
If the sum equals the target, return the indices.
If the sum is less than the target, move the left pointer to the right.
If the sum is greater than the target, move the right pointer to the left.

## Key Concepts
- Employs two indices traversing the data structure.  
- Can move pointers towards each other or at different strides.  
- Improves efficiency by reducing time complexity.

## Summary
The two pointers technique is a powerful and versatile method for solving array and string problems efficiently.
