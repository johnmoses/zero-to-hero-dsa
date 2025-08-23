# Search in Rotated Sorted Array - Python Example

def search_rotated(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        if arr[low] <= arr[mid]:  # left half is sorted
            if arr[low] <= target < arr[mid]:
                high = mid-1
            else:
                low = mid+1
        else:  # right half sorted
            if arr[mid] < target <= arr[high]:
                low = mid+1
            else:
                high = mid-1
    return -1

arr = [4,5,6,7,0,1,2]
print("Index of 0:", search_rotated(arr, 0))
