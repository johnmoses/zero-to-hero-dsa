# Binary Search - Python Example

def binary_search(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return -1

arr = [1,2,3,4,5,6,7]
print("Index of 4:", binary_search(arr, 4))
