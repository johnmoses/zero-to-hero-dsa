""" 
Quick Sort using list comprehension

Sample Input: [64, 34, 25, 12, 22, 11, 90, 5]

Sample Output: [5, 11, 12, 22, 25, 34, 64, 90]
"""
def quickSort1(arr):
    """
    Sorts an array using the Quick Sort algorithm.

    Args:
        arr (list): The array to be sorted.

    Returns:
        list: The sorted array.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quickSort1(left) + [pivot] + quickSort1(right)

def quickSort2(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quickSort2(left) + [pivot] + quickSort2(right)

print(quickSort1([64, 34, 25, 12, 22, 11, 90, 5]))
print(quickSort2([64, 34, 25, 12, 22, 11, 90, 5]))
