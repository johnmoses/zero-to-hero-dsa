# Monotonic Queues

## Introduction
Monotonic queues maintain elements in a sorted order (increasing or decreasing) and support efficient sliding window maximum or minimum.

## Details
They offer O(n) solutions for sliding window problems by pushing and popping elements to maintain the queue’s order.

Monotonic queues enable quick retrieval of extremal values in windows without sorting.

## Examples
Finding maximum in every sliding window of a fixed size.

## Key Concepts
- Queue maintains order for sliding windows.  
- Push new elements and pop obsolete or smaller/larger elements.  
- Efficient for range maximum/minimum problems.

## Summary
Monotonic queues solve sliding window problems efficiently using ordered queue operations.
