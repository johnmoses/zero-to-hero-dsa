"""
Given a set of numbers, write a divide and conquer algorithm to sort the numbers.

Example 1:
    Input: [3, 7, 6, -10, 15, 23.5, 55, -13]
    Output: [-13, -10, 3, 6, 7, 15, 23.5, 55]
"""
def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(arr):
    # Base case - array of size 1 or less is already sorted
    if len(arr) <= 1:
        return arr
        
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

print(merge_sort([3, 7, 6, -10, 15, 23.5, 55, -13]))