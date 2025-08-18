"""
Given a set of numbers, write a divide and conquer algorithm to sort the numbers.

Example 1:
    Input: [3, 7, 6, -10, 15, 23.5, 55, -13]
    Output: [-13, -10, 3, 6, 7, 15, 23.5, 55]
"""
def merge_sort(arr):
    """
    This algorithm runs in O(n log n) time and is stable with O(n) extra space.
    It sorts an array using the merge sort technique, which is a classic divide and conquer algorithm.
    """
    # Base case: when the array has 0 or 1 element, it is already sorted
    if len(arr) <= 1:
        return arr

    # Divide: split the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Conquer & Combine: merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = j = 0

    # Merge two sorted arrays into one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add any remaining elements from left and right
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


print(merge_sort([3, 7, 6, -10, 15, 23.5, 55, -13]))