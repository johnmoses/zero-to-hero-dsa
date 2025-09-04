# Fixed Size Sliding Window

## Introduction
The fixed size sliding window technique involves moving a window of fixed length across a data structure to analyze or aggregate information within the window.

## Details
It efficiently computes values like sums, maximums, or averages over subarrays or substrings of a fixed size by updating calculations as the window slides.

It avoids recomputing from scratch by subtracting the element leaving the window and adding the new element entering.

## Examples
Finding the maximum sum of any contiguous subarray of size k.
Example:
Input: arr = [2, 1, 5, 1, 3, 2], k = 3
Output: 9
Explanation:
1. Calculate the sum of the first 'k' elements to initialize the window.
2. Slide the window across the array by adding the next element and removing the first element of the previous window.
3. Keep track of the maximum sum encountered during the sliding process.    

## Key Concepts
- Sliding window size stays constant.  
- Efficient updating of aggregates.  
- Common in problems involving subarrays/substrings.

## Summary
Fixed size sliding window optimizes repetitive computations on continuous segments of data.
