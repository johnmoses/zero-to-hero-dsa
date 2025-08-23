# Array Operations - Python Example

arr = [1, 2, 3, 4, 5]

# Traversal
for element in arr:
    print("Element:", element)

# Insertion (append)
arr.append(6)

# Deletion (remove by value)
arr.remove(2)

# Searching (index)
index = arr.index(4) if 4 in arr else -1
print("Index of 4:", index)

# Updating
arr[0] = 10
print("Updated array:", arr)
