
""" 
Find start index of a rotated non-decreasing array
"""

def findStartIndex(arr):
    # Initialize low pointer lo, high pointer hi to n-1
    lo = 0
    hi = len(arr) - 1

    # Iterate over array and do a binary search approach
    while lo <= hi:
        mid = (lo + hi) // 2

        if arr[mid] <= arr[hi]:
            hi = mid - 1
        else:
            lo = mid + 1

    return lo

print(findStartIndex([3, 4, 5, 1, 2]))
# Output: 3