# Introduction to Big O Notation

## Introduction
Big O notation describes how the performance of an algorithm changes with input size. It helps analyze time and space complexity.

## Details
Big O measures worst-case scenarios for an algorithm’s growth rate.

Common complexities:

- O(1): Constant time (super fast, doesn’t depend on input size).
- O(log n): Logarithmic time (fast but slows down as input grows).
- O(n): Linear time (scales directly with the input size).
- O(n log n): Linearithmic time (common in sorting algorithms).
- O(n²): Quadratic time (loops inside loops).
- O(2^n): Exponential time (the dreaded brute force recursion).


Understanding these classes is essential for choosing efficient algorithms.

## Examples
Example time complexities:

# Python
def constant_time(items):
    return items[0]  # O(1)

def linear_time(items):
    s = 0
    for item in items:
        s += item  # O(n)
    return s

## Key Concepts
- Big O measures algorithm efficiency.  
- Focuses mainly on input size impact.  
- Helps predict scalability.

## Summary
Big O notation is a powerful tool to understand and compare algorithm efficiency, guiding developers to optimize performance.
