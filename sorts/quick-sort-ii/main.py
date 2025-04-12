""" 
Quick Sort

Sample Input: [64, 34, 25, 12, 22, 11, 90, 5]

Sample Output: [5, 11, 12, 22, 25, 34, 64, 90]
"""

# Find the partition position
def partition(array, low, high):
    
    # Choose the rightmost item as pivot
    pivot = array[high]

    # Set pointer for greater item
    i = low - 1

    # Traverse through all items
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:

            # If item smaller than pivot is found
            # swap it with the greater item pointed by i
            i = i + 1

            # Swapping item at i with item at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot item with the greater item specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1

# function to perform quicksort


def quickSort(array, low, high):
    if low < high:

        # Find pivot item such that
        # item smaller than pivot are on the left
        # item greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)

