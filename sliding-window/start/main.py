""" 
Write a sliding window algorithm with explanation.

Example 1:
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    window_size = 3
"""
def sliding_window_sum(arr, window_size):
    """
    Calculates the sum of the elements in a sliding window of given size.

    Args:
        arr: The input array.
        window_size: The size of the sliding window.

    Returns:
        A list of sums of the sliding windows.
    """
    window_sums = []

    # Calculate the sum of the first window
    current_sum = sum(arr[:window_size])
    window_sums.append(current_sum)

    # Slide the window over the array
    for i in range(window_size, len(arr)):
        # Remove the element at the left end of the window
        current_sum -= arr[i-window_size]
        # Add the element at the right end of the window
        current_sum += arr[i]
        window_sums.append(current_sum)

    return window_sums

print(sliding_window_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
