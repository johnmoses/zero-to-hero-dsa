"""
Binary search examples
"""

arr1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
arr2 = ['A','B','D','G','C','F','E']
target1 = 9
target2 = 'B'

def binary_search(arr, target):
    # Initialize variables
    left = 0
    n = len(arr)
    right = n - 1

    # Iterate over arr
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(binary_search(arr1, target1))
print(binary_search(arr2, target2))

def binary_search_1(arr, target):
    # Initialize variables
    left = 0
    n = len(arr)
    right = n - 1

    # Iterate over array
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid

print(binary_search_1(arr1, target1))
print(binary_search_1(arr2, target2))