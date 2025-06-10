# Prefix Sum

The prefix sum is a technique used to efficiently calculate the sum of all elements in an array up to a specified index. It is also known as cumulative sum

What it does is to  pre-compute the sum of all elements up to each index in the array and then use these pre-computed sums to quickly calculate the sum of any sub-array in the array.

It has time complexity of O(n) and a space complexity of O(n), it is efficient and widely used in various computational problems such as range sum queries, dynamic programming and more.

## When to use

- To efficiently perform multiple sum queries on a subarray or need to calculate cumulative sums
- Cumulative sums are needed from index 0 to any element
- Querying subarray sums frequently across multiple ranges
- Partial sums can be reused efficiently

## Efficiency

A subarray sum would take O(N). A Q subarrays sum would take O(N*Q)

## Problems

- Range Sum Query — Immutable (LeetCode #303)
- Contiguous Array (LeetCode #525)
- Subarray Sum Equals K (LeetCode #560)
