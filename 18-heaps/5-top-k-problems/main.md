# Top K Problems Using Heaps

## Introduction
Top K problems require finding the K largest or smallest elements from a dataset efficiently. Heaps are ideal for these problems due to their dynamic ordering properties.

## Details
The common approach uses a min-heap of size K to maintain the current top K elements. For every new element:

- If heap size is less than K, add element.  
- Else if the new element is larger than the smallest in the heap (root), remove root and add new element.

At the end, heap contains the top K elements.

This ensures O(N log K) runtime efficiency for N elements.

## Examples
Finding the top K largest numbers in an unsorted array.

## Key Concepts
- Use min-heap to maintain top K largest efficiently.  
- Supports streaming data scenarios.  
- Optimal time complexity compared to sorting entire data.

## Summary
Heaps provide an elegant, efficient solution for Top K element problems frequently encountered in interviews and applications.
