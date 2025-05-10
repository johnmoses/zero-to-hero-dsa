# Siding Window

This is a problem-solving technique that’s designed to transform two nested loops into a single loop. In other words it is used to find a sub-array or sub-string that satisfies a specific condition. This is mostly done done by defining a window or range in the input data (arrays or strings) and then moving that window across the data to perform some operation within the window.

Sliding window algorithms are mostly used in scenerios like finding subarrays with a specific sum, finding the longest substring with unique characters, running average, target value identification, or solving problems that require a fixed-size window to process elements efficiently

## Efficiency

Sliding window problems are very easy to solve using a brute force approach in O(n²) or O(n³). However, the sliding window technique can reduce the time complexity of an algorithm to O(n).

## When to use

- When dealing with problems involving contiguous sub-arrays or sub-strings

## Sample problems

Maximum Average Subarray I (LeetCode #643)
Longest Substring Without Repeating Characters (LeetCode #3)
Minimum Window Substring (LeetCode #76)

Referrences

- <https://builtin.com/data-science/sliding-window-algorithm>
