# Fixed Size Sliding Window

## Introduction
The fixed size sliding window technique involves moving a window of fixed length across a data structure to analyze or aggregate information within the window.

## Details
It efficiently computes values like sums, maximums, or averages over subarrays or substrings of a fixed size by updating calculations as the window slides.

It avoids recomputing from scratch by subtracting the element leaving the window and adding the new element entering.

## Examples
Finding the maximum sum of any contiguous subarray of size k.

## Key Concepts
- Sliding window size stays constant.  
- Efficient updating of aggregates.  
- Common in problems involving subarrays/substrings.

## Summary
Fixed size sliding window optimizes repetitive computations on continuous segments of data.
