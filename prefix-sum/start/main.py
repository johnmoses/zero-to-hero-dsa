""" 
Example for Prefix Sum in Python

The prefix sum of an array at index 'i' is the sum of all numbers from index '0' to 'i'. 
By computing and storing the prefix sum of an array, you can easily answer queries about the sum of any subarray in constant time
"""
def prefix_sum_array(arr):
    prefix_sum = [0]
    for num in arr:
        prefix_sum.append(prefix_sum[-1] + num)
    return prefix_sum

print(prefix_sum_array([1, -20, -3, 30, 5, 4]))