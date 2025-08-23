# Heap Operations

## Introduction
Heap operations are fundamental to maintaining the heap data structure and include inserting an element, extracting the root (min or max), heapify, and peeking at the root.

## Details
- **Insert:** Add element to the end and sift-up to restore heap property.  
- **Extract:** Remove root element, replace it with last element, then sift-down to maintain heap property.  
- **Heapify:** Build a heap from an unsorted array, usually in O(n) time by repeatedly fixing heap property from bottom up.  
- **Peek:** Retrieve the root element (minimum in min-heap, maximum in max-heap) without removing it.

These operations allow heaps to efficiently support priority queue functionality.

## Examples
Building a max heap from an array by heapifying, then inserting and extracting elements.

## Key Concepts
- Sift-up and sift-down are used to fix heap violations.  
- Heapify efficiently constructs a heap from an unsorted array.  
- Root always contains the highest or lowest priority element.

## Summary
Understanding heap operations is essential to use heaps effectively in algorithm design and priority management.
