""" 
Search algorithm

Write a basic search algorithm with step by step explanation.

Example 1:
    my_list = [10, 5, 20, 15, 30]
    target_value = 15
"""

def linear_search(arr, target):
    """
    Performs a linear search on a list.

    Args:
        arr: The list to search.
        target: The value to search for.

    Returns:
        The index of the target if found, otherwise -1.
    """
    # 1. Iterate through each element of the list.
    for i in range(len(arr)):
        # 2. Check if the current element is equal to the target.
        if arr[i] == target:
            # 3. If found, return the index.
            return i
    # 4. If the loop finishes without finding the target, return -1.
    return -1

print(linear_search([10, 5, 20, 15, 30], 15))