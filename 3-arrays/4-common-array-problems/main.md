# Common Array Problems

## Introduction
Arrays are involved in many classical algorithmic problems such as finding maximum/minimum, sorting, searching, and subarray challenges.

## Details
Typical problems include:

- Finding the maximum or minimum element.
- Reversing an array.
- Finding subarrays with certain properties (e.g., maximum sum subarray).
- Searching for an element efficiently.
- Removing duplicates.

Understanding these problems and their solutions improves algorithmic thinking.

## Examples
Finding maximum element by traversal:

max_val = arr[0]  
for val in arr:  
    if val > max_val: max_val = val

Reversing an array:
reversed_arr = arr[::-1]

Finding maximum sum subarray (Kadane's Algorithm):
max_current = max_global = arr[0]  
for val in arr:  
    max_current = max(val, max_current + val)  
    max_global = max(max_global, max_current)

Searching for an element:
def binary_search(arr, target):  
    left, right = 0, len(arr) - 1  
    while left <= right:  
        mid = (left + right) // 2  
        if arr[mid] == target:  
            return mid  
        elif arr[mid] < target:  
            left = mid + 1  
        else:  
            right = mid - 1  
    return -1  

Removing duplicates:
unique_arr = list(set(arr))


## Key Concepts
- Use iterative approaches for linear problems.  
- Utilize sorting to simplify some problems.  
- Apply sliding window or two-pointer techniques for subarrays.

## Summary
Practicing common array problems builds a strong foundation for more advanced algorithm challenges.
