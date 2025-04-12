""" 
Radix Sort

This sorts an array by individual digits, starting with the least significant digit (the rightmost one).

Sample Input: [170, 45, 75, 90, 802, 24, 2, 66]

Sample Output: [2, 170, 45, 24, 75, 90, 66, 802]
"""
def radixSort(arr):
    """
    Sorts an array using the Radix Sort algorithm.

    Args:
        arr (list): The array to be sorted.

    Returns:
        list: The sorted array.
    """
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr

def counting_sort(arr, exp):
    """
    Helper function for Radix Sort.

    Args:
        arr (list): The array to be sorted.
        exp (int): The current digit position being sorted.

    Returns:
        None
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

print(radixSort([170, 45, 75, 90, 802, 24, 2, 66]))