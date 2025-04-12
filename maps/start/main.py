""" 
Maps
Write a basic example of map data structure to show basic operations
"""

# Create an empty map or dictionary
m = {}

# Add key-value pairs to the map
m["a"] = 1
m["b"] = 2
m["c"] = 3

# Print the map
print(m)  # Output: {'a': 1, 'b': 2, 'c': 3}  
print(m["a"])  # Output: 1

# Check if a key exists in the map
print("a" in m)  # Output: True

# Remove a key-value pair from the map
del m["a"]
print(m)  # Output: {'b': 2, 'c': 3}
print("a" in m)  # Output: False
print("b" in m)  # Output: True

# Iterate over the map
for key, value in m.items():
    print(key, value)

# Output:
    # ('b', 2)
# ('c', 3)

# Iterate over the keys in the map
for key in m.keys():
    print(key)

# Output:
    # b
    # c

# Iterate over the values in the map
for value in m.values():
    print(value)
    # Output:
    # 2
    # 3

# Iterate over the keys in the map using a list comprehension
for key in [k for k in m.keys()]:
    print(key)
    # Output:
    # b
    # c

# Iterate over the values in the map using a list comprehension
for value in [v for v in m.values()]:
    print(value)
    # Output:
    # 2
    # 3

# Iterate over the keys in the map using a list comprehension and sorted
for key in sorted([k for k in m.keys()]):
    print(key)
    # Output:
    # b
    # c

# Iterate over the values in the map using a list comprehension and sorted
for value in sorted([v for v in m.values()]):
    print(value)
    # Output:
    # 2
    # 3

