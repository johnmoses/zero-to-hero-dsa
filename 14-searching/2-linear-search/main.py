# Linear Search - Python Example

def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

arr = [5,3,1,9,7]
print("Index of 9:", linear_search(arr, 9))
