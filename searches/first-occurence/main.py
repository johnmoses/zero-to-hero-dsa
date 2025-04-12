"""
Find first occurance of a number in a sorted array (increasing order)
Approach- Binary Search
T(n)- O(log n)
"""

arr1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
arr2 = ['A','B','D','G','C','F','E']
target1 = 9
target2 = 'B'

def first_occurrence(arr, target):
    # Initialize variables
    left = 0
    right = len(arr) -1

    # Iterate over array
    while left <= right:
        mid = left + (right - left) // 2
        if left == right:
            break
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    if arr[left] == target:
        return left

print(first_occurrence(arr1, target1))
print(first_occurrence(arr2, target2))