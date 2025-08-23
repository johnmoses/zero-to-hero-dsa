# Segment Trees

## Introduction

Segment Trees are advanced data structures used for efficient range queries and updates on arrays. They allow querying and modifying elements in logarithmic time, making them ideal for dynamic scenarios.

## Details

A Segment Tree is a binary tree where each node represents a segment (subarray) of the original array. Internal nodes combine information from their child segments, supporting queries such as sum, minimum, maximum, and more.

Key operations:

- **Build:** Constructing the tree from the initial array in O(n) time.
- **Query:** Retrieving information (e.g., sum) over a range in O(log n).
- **Update:** Modifying an element or a range and updating tree nodes in O(log n).

Segment Trees can be extended to support lazy propagation for efficient range updates.

## Examples

Common use cases include:

- Range sum or minimum queries.
- Updating array elements dynamically.
- Interval problems in competitive programming.

## Key Concepts

- Tree representation of array segments.
- Recursive construction and querying.
- Lazy propagation for bulk updates.
- Space complexity O(4*n) for safe tree size allocation.

## Summary

Segment Trees provide an efficient way to handle range queries and point or range updates on arrays. Mastery of segment trees enables solving problems involving dynamic data with logarithmic time complexities.
