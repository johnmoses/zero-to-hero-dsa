
""" 
Find start index of a rotated non-decreasing array
"""

def findStartIndex(arr):
    # Initialize length of array n, low pointer lo, high pointer hi to n-1
    n = len(arr)
    lo = 0
    hi = n - 1

    # Iterate over array and do a binary search approach
    while lo <= hi:
        mid = (lo + hi) // 2

        if arr[mid] <= arr[n - 1]:
            hi = mid - 1
        else:
            lo = mid + 1

    return lo

print(findStartIndex([3, 4, 5, 1, 2]))
# Output: 3