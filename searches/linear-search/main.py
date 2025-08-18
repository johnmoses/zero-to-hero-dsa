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

def linearSearch(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

print(linearSearch([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 9))
print(linearSearch(['A','B','D','G','C','F','E'], 'B'))