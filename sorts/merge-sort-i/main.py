""" 
Merge Sort
This is a divide-and-conquer algorithm that sorts an array 
by first breaking it down into smaller arrays, 
and then building the array back together the correct way so that it is sorted.

Sample Input: [3, 7, 6, -10, 15, 23.5, 55, -13]

Sample Output:
    [-13, -10, 3, 6, 7, 15, 23.5, 55]
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    return merge(sorted_left, sorted_right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

print(merge_sort([3, 7, 6, -10, 15, 23.5, 55, -13]))