""" 
Exponential Search
"""

def binary_search(arr, target, left, right):
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def exponential_search(arr, target):
    if not arr:
        return -1
    if arr[0] == target:
        return 0
    
    index = 1
    while index < len(arr) and arr[index] <= target:
        index *= 2
    
    return binary_search(arr, target, index // 2, min(index, len(arr) - 1))

# Example usage
arr = [10, 12, 15, 17, 18, 19, 21, 23, 24, 33, 35, 42, 47, 50]
target = 18
result = exponential_search(arr, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the array")