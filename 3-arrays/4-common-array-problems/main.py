# Common Array Problems - Python Example

arr = [1, 3, 2, 8, 5]

# Find maximum
max_val = arr[0]
for val in arr:
    if val > max_val:
        max_val = val
print("Maximum value:", max_val)

# Find maximum subarray sum
max_current = max_global = arr[0]  
for val in arr:  
    max_current = max(val, max_current + val)  
    max_global = max(max_global, max_current)  
print("Maximum subarray sum:", max_global)


# Reverse array
reversed_arr = arr[::-1]
print("Reversed array:", reversed_arr)

# Sum of subarray [1:4]
sub_sum = sum(arr[1:4])
print("Subarray sum:", sub_sum)

# Search for an element
def binary_search(arr, target):  
    left, right = 0, len(arr) - 1  
    while left <= right:  
        mid = (left + right) // 2  
        if arr[mid] == target:  
            return mid  
        elif arr[mid] < target:  
            left = mid + 1  
        else:  
            right = mid - 1  
    return -1  
print("Element found at index:", binary_search(sorted(arr), 5))

# Remove duplicates
unique_arr = list(set(arr))
print("Array without duplicates:", unique_arr)

# Sort array
sorted_arr = sorted(arr)
print("Sorted array:", sorted_arr)