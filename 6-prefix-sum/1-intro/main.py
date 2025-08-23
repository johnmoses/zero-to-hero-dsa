# Prefix Sum - Python Example

def prefix_sum(arr):
    prefix = [0] * len(arr)
    prefix = arr
    for i in range(1, len(arr)):
        prefix[i] = prefix[i-1] + arr[i]
    return prefix

arr = [1, 2, 3, 4]
prefix = prefix_sum(arr)
print("Prefix sum array:", prefix)
# Sum of range 1 to 3:
result = prefix[3] - prefix
print("Sum from index 1 to 3:", result)
