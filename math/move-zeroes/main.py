"""
Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements.

Sample Input: [0, 1, 0, 3, 12]
Sample Output: [1, 3, 12, 0, 0]

The time complexity of the below algorithm is O(n).
"""
def moveZeroesToEnd1(arr):
    # Initialize index to track non-zero elements
    non_zero_idx = 0
    
    # Move non-zero elements to the front
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_idx], arr[i] = arr[i], arr[non_zero_idx]
            non_zero_idx += 1

    return arr

def moveZeroesToEnd2(array):
    # Define and initialize result res and zeroes
    res = []
    zeros = 0

    # Iterate over the array
    # Check for zeros and non-boolean values
    for i in array:
        if isinstance(i, int) and i == 0:
            zeros += 1
        else:
            res.append(i)
    res.extend([0] * zeros)
    return res

print(moveZeroesToEnd1([0, 1, 0, 3, 12]))
print(moveZeroesToEnd2([0, 1, 0, 3, 12]))