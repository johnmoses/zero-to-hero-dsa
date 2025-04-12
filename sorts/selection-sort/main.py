""" 
Selection sort

Given an array, [5, 3, 6, 2, 10], write a selection sort algorithm to sort the array in ascending order.
The output should be [2, 3, 5, 6, 10]
"""
def selection_sort1(arr):
    for i in range(len(arr)):
        # Initialize minimum index
        min_index = i
        for j in range(i+1, len(arr)):
            # Update minimum index conditionally
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap current index with minimum element in rest of list
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort1([5, 3, 6, 2, 10]))