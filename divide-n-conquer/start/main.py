"""
Write a basic divide and conquer algorithm to recursively summ elements in an array

Sample 1:
    Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    Output: 55
    Explanation: The sum of the array is 55.
"""

def divide_and_conquer(arr):
    """
    Basic divide and conquer algorithm example.
    This function demonstrates the concept by recursively summing the elements of an array.

    Args:
        arr: The input array of numbers.

    Returns:
        The sum of the elements in the array.
    """
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]

    mid = len(arr) // 2
    left_sum = divide_and_conquer(arr[:mid])
    right_sum = divide_and_conquer(arr[mid:])

    return left_sum + right_sum

result = divide_and_conquer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"The sum of the array is: {result}")
