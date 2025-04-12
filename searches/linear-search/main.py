"""
Linear search
The Linear Search algorithm searches through an array and returns the index of the value it searches for.
T(n): O(n)

Example 1:
arr1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target1 = 9

Example 2
arr2 = ['A','B','D','G','C','F','E']
target2 = 'B'
"""

def linearSearch1(arr, target):
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return i
    return -1


def linearSearch2(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

print(linearSearch1([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 9))
print(linearSearch2([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 9))

print(linearSearch1(['A','B','D','G','C','F','E'], 'B'))
print(linearSearch2(['A','B','D','G','C','F','E'], 'B'))