# Difference Arrays

## Introduction
Difference arrays are a powerful technique to perform range update queries efficiently on arrays.

## Details
By recording the difference between consecutive elements, updates on a range become constant time operations.

The actual array can be reconstructed by computing the prefix sums of the difference array.

## Examples
To add 5 to all elements between indices 1 and 3:

- Increment difference_array[1] by 5  
- Decrement difference_array by 5 (if within range)

## Key Concepts
- Supports fast range updates.  
- Uses difference array and prefix sums relation.  
- Helpful in interval and batch update problems.

## Summary
Difference arrays optimize batch range modifications by leveraging the prefix sum concept inversely.
