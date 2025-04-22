""" 
Create a basic hash table to store adn access fruits based on their first letters.
"""
# Create an empty map or dictionary
m = {}

# Add key-value pairs to the map
m["a"] = "apple"
m["b"] = "banana"
m["c"] = "cherry"

# Print the map
print(m)  # Output: {'a': 'apple', 'b': 'banana', 'c': 'cherry'}
print(m["a"])  # Output: apple

# Check if a key exists in the map
print("a" in m)  # Output: True

# Remove a key-value pair from the map
del m["a"]
print(m)  # Output: {'b': 'banana', 'c': 'cherry'}
print("a" in m)  # Output: False
print("b" in m)  # Output: True

# Iterate over the map
for key, value in m.items():
    print(key, value)

# Output:
    # ('b', 'banana')
# ('c', 'cherry')

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
    # banana
    # cherry

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
    # banana
    # cherry

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
    # banana