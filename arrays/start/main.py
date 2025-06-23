"""
Arrays

Getting started with arrays
"""

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# All array elements
print(arr)

# Selecting
print('0: ', arr[0])
print('1: ', arr[1])
print('2: ', arr[2])
print('3: ', arr[3])
print('4: ', arr[4])

# Slicing
print('-1: ', arr[-1])
print('1: ', arr[1:])
print(':4: ', arr[:4])
print('1:3: ', arr[1:3])
print('::2: ', arr[::2])
print('::-1: ', arr[::-1])
print('1:4:2: ', arr[1:4:2])
print('1::2: ', arr[1::2])

# Sequence operations
print('Index 3: ', arr.index(3))
print('Count at 3: ', arr.count(3))
print(arr)

# Add item to end
arr.append(11)
print('Append 11: ', arr)

# Add at specified index
arr.insert(0, 0)
print('Insert 0 at 0: ', arr)

# Remove item
arr.remove(0)
print('Remove at 0: ', arr)

# Remove top item
arr.pop()
print('Pop: ', arr)
arr.pop(0)
print('Pop at 0: ', arr)

# Sort items
arr.sort()
print('Sort: ', arr)

# Search item
print('Index of 5: ', arr.index(5))

# Reverse order
arr.reverse()
print('Reverse: ', arr)

# Lenght of array
print('Len: ', len(arr))

# Maximum element
print('Max: ', max(arr))

# Minimum element
print('Min: ', min(arr))

# Sum of elements
print('Sum: ', sum(arr))
print('Sum/len: ', sum(arr) / len(arr))

# Remove all items
arr.clear()
