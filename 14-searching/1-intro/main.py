# Searching Introduction - Python Example

def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid -1
    return -1

arr = [2,4,6,8,10]
print("Linear search index:", linear_search(arr, 8))
print("Binary search index:", binary_search(arr, 8))
