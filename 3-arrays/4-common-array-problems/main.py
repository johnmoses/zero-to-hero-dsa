# Common Array Problems - Python Example

arr = [1, 3, 2, 8, 5]

# Find maximum
max_val = arr[0]
for val in arr:
    if val > max_val:
        max_val = val
print("Maximum value:", max_val)

# Reverse array
reversed_arr = arr[::-1]
print("Reversed array:", reversed_arr)

# Sum of subarray [1:4]
sub_sum = sum(arr[1:4])
print("Subarray sum:", sub_sum)
