# Binary Search

Bimary search algorithm is one of the most efficient search algorithms in computing. The algorithms itself is made up of the folliwing components:

- Target: search value or parameter
- Index: current location
- Left, right, start, end, low, high: indices of the search space
- Mid: index of search condition

## Parts of efficient binary search algorithms

Efficient binary search algorithms are typically composed of three parts:

1. Pre-processing to do a sort if collection is unsorted
2. Searching with loop or recursion to divide search space into two after each comparison
3. Post-processing to determine viable candidates in the remaining search space

Binary search algorithms can be implemented both iteratively and recursively. However, the major difference is that the iterative version of binary search uses O(1) memory while the recursive version uses O(log(N)) memory.

## Binary Search Patterns

Looking at binary search coding patterns, three templates can be deduced. This includes basic, advanced and professional patterns

## Modified Binary Search

Modified Binary Search pattern adapts binary search to solve a wider range of problems, such as finding elements in rotated sorted arrays.

Use this pattern for problems involving sorted or rotated arrays where you need to find a specific element.

## Modified Binary Search Problems

- Search in Rotated Sorted Array (LeetCode #33, Grind, Blind)
- Find Minimum in Rotated Sorted Array (LeetCode #153, Blind)
- Search a 2D Matrix II (LeetCode #240)
