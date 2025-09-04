# Introduction to Prefix Sum

## Introduction
Prefix Sum is a technique that preprocesses an array to enable efficient range sum queries.

It is used to efficiently calculate the sum of all elements in an array up to a specified index. It is also known as cumulative sum

What it does is to  pre-compute the sum of all elements up to each index in the array and then use these pre-computed sums to quickly calculate the sum of any sub-array in the array.

## Details
It involves creating an auxiliary array where each element at index i is the sum of all elements from the start to i.

With prefix sums, you can find the sum of any subarray in constant time by subtracting prefix sums.

## Efficiency
It has time complexity of O(n) and a space complexity of O(n), it is efficient and widely used in various computational problems such as range sum queries, dynamic programming and more. A subarray sum would take O(N). A Q subarrays sum would take O(N*Q)

## Examples
Prefix sum array for [1,2,3,4] is [1,3,6,10].

Sum of elements from index 1 to 3 is prefix[3] - prefix = 10 - 1 = 9.

## Key Concepts
- Preprocessing array for quick sum queries.  
- Trade-off between preprocessing time and query efficiency.  
- Useful in many algorithmic problems.

## Summary
Prefix sum transforms range sum queries to O(1) operations after O(n) preprocessing.
