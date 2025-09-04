# Hashing - Python Example

hash_map = {}

# Insert
hash_map["apple"] = 3
hash_map["banana"] = 5

# Lookup
print("Apple count:", hash_map.get("apple", 0))

# Update
hash_map["apple"] += 2
print("Updated apple count:", hash_map["apple"])

dct = {}

# Add key-value pairs to the dictionary
dct["a"] = 1
dct["b"] = 2
dct["c"] = 3

# Print the dictionary
print(dct)  # Output: {'a': 1, 'b': 2, 'c': 3}  
print(dct["a"])  # Output: 1

# Check if a key exists in the dictionary
print("a" in dct)  # Output: True

# Remove a key-value pair from the dictionary
del dct["a"]
print('Deleted a: ', dct)  # Output: {'b': 2, 'c': 3}
print("a" in dct)  # Output: False
print("b" in dct)  # Output: True

# Iterate over items in the dictionary
print('Items')
for item in dct.items():
    print('item: ', item)

# Iterate over the keys and values dictionary
print('Keys and values:')
for key, value in dct.items():
    print(key, value)

# Iterate over the keys in the dictionary
print('Keys:')
for key in dct.keys():
    print(key)

# Iterate over the values in the dictionary
print('Values:')
for value in dct.values():
    print(value)

# Iterate over the keys in the dictionary using a list comprehension
print('Keys with list comprehension:')
for key in [k for k in dct.keys()]:
    print(key)

# Iterate over the values in the dictionary using a list comprehension
print('Values with list comprehension:')
for value in [v for v in dct.values()]:
    print(value)
