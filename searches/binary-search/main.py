"""
Binary search examples
"""

arr1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target1 = 9
arr2 = ['A','B','D','G','C','F','E']
target2 = 'B'

def binary_search1(arr, target):
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

print(binary_search1(arr1, target1))
print(binary_search1(arr2, target2))

def binary_search2(arr, target):
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

print(binary_search2(arr1, target1))
print(binary_search2(arr2, target2))