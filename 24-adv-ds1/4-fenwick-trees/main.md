# Fenwick Trees (Binary Indexed Trees)

## Introduction

Fenwick Trees, also known as Binary Indexed Trees (BIT), are data structures that efficiently support prefix sum queries and updates on an array. They provide a simple and space-efficient alternative to segment trees for cumulative frequency operations.

## Details

A Fenwick Tree stores partial sums allowing both updates to elements and prefix sum queries in O(log n) time. It uses bitwise operations to traverse and update nodes in a compact tree structure.

Key operations:

- **Update:** Add a value to an element and propagate the change.
- **Query:** Compute the prefix sum up to a given index.

Fenwick Trees are optimal for scenarios requiring frequent point updates and prefix queries, offering quicker implementation and less memory than segment trees.

## Examples

Fenwick Trees are commonly used for:

- Range sum queries (prefix sums).
- Counting inversions in arrays.
- Frequency counting in dynamic datasets.

## Key Concepts

- Efficient traversal using bit manipulation.
- Supports point updates and prefix queries.
- Space complexity O(n).
- Simple and cleaner implementation compared to segment trees.

## Summary

Fenwick Trees provide an elegant solution for managing prefix sums and updates, making them a valuable data structure for many algorithmic problems involving cumulative data.
