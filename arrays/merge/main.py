"""
Merge two Arrays into one
Do not return anything, modify in-place

arr1 = [1,2,3,0,0,0]
arr2 = [2,5,6]
m = 3
n = 3
"""

def merge1(arr1, arr2, m, n):
    # Iterate over arr2
    for i in range(n):
        # Update value of arr1 after index m to value of arr2 at index i
        arr1[i+m] = arr2[i]

    # Sort list in-place
    arr1.sort()
    print(arr1)

def merge2(arr1, arr2, m, n):
    # Initialize pointers for arr1 and arr2
    p1 = m - 1  # Last non-zero element in arr1
    p2 = n - 1  # Last element in arr2
    p = m + n - 1  # Last position in arr1
    
    # Merge arrays from end to start
    while p2 >= 0:
        if p1 >= 0 and arr1[p1] > arr2[p2]:
            arr1[p] = arr1[p1]
            p1 -= 1
        else:
            arr1[p] = arr2[p2]
            p2 -= 1
        p -= 1

    print(arr1)


print(merge1([1,2,3,0,0,0], [2,5,6], 3, 3))
print(merge2([1,2,3,0,0,0], [2,5,6], 3, 3))