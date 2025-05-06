""" 
Search algorithm

Write a basic search algorithm to find the index of a value in a list.

Example 1:
    my_list = [10, 5, 20, 15, 30]
    target_value = 15
"""

def linear_search(arr, target):
    # Iterate through each element of the list.
    for i in range(len(arr)):
        # Check if the current element is equal to the target.
        if arr[i] == target:
            # If found, return the index.
            return i
    # If the loop finishes without finding the target, return -1.
    return -1

print(linear_search([10, 5, 20, 15, 30], 15))