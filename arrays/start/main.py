"""
Arrays

Write code to show the basic functionality or behavior of an array
"""

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# All array elements
print(arr)

# Select element by index
print('Selecting')
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
print(arr[4])

print('Slicing')
print(arr[-1])
print(arr[1:])
print(arr[:4])
print(arr[1:3])
print(arr[::2])
print(arr[::-1])
print(arr[1:4:2])
print(arr[1::2])


# Add item to end
print('Adding')
arr.append(11)
print(arr)

# Add at specified index
arr.insert(0, 0)
print(arr)

# Remove item
print('Removing')
arr.remove(0)
print(arr)

# Remove top item
arr.pop()
print(arr)
arr.pop(0)
print(arr)

# Sort items
print('Sorting')
arr.sort()
print(arr)

# Reverse order
arr.reverse()
print(arr)

# Item at specified index
print(arr.index(3))
print(arr.count(3))
print(arr)

# Lenght of array
print(len(arr))

# Maximum element
print(max(arr))

# Minimum element
print(min(arr))

# Sum of elements
print(sum(arr))
print(sum(arr) / len(arr))

# Remove all items
arr.clear()
