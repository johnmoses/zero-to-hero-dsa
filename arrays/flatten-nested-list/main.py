""" 
Write code to flatten a nested list.
"""
def flatten_list1(nested_list):
    """
    Flatten a nested list into a single list.

    Args:
        nested_list (list): A nested list to be flattened.

    Returns:
        list: A flattened list containing all elements from the nested list.
    """
    # Initialize an empty list to store the flattened elements
    flattened = []

    # Iterate over each element in the nested list
    for element in nested_list:
        # Check if the current element is a list
        if isinstance(element, list):
            # If it is a list, recursively flatten it and extend the flattened list
            flattened.extend(flatten_list1(element))
        else:
            # If it is not a list, append the element to the flattened list
            flattened.append(element)

    # Return the flattened list
    return flattened

print(flatten_list1([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))