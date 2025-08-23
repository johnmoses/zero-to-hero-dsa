# Search Problem Examples - Python Example

def count_ones(arr):
    low, high = 0, len(arr)-1
    count = 0
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == 1:
            count = len(arr) - mid
            high = mid - 1
        else:
            low = mid + 1
    return count

arr = [0,0,0,1,1,1,1]
print("Count of ones:", count_ones(arr))
