""" 
Write a basic example of set data structure with basic functionalities
"""
# Creating a set
my_set = {1, 2, 3, 4, 5}
print("Original set:", my_set)

# Adding elements to the set
my_set.add(6)
print("After adding 6:", my_set)
my_set.update([7, 8, 9])
print("After updating with [7, 8, 9]:", my_set)

# Removing elements from the set
my_set.remove(3)
print("After removing 3:", my_set)
my_set.discard(8)
print("After discarding 8:", my_set)

# Checking if an element is in the set
print("Is 4 in the set?", 4 in my_set)
print("Is 10 in the set?", 10 in my_set)

# Set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference:", set1.difference(set2))
print("Symmetric difference:", set1.symmetric_difference(set2))

# Create a set of integers
my_set = {1, 2, 3, 4, 5, 5, 5}  # Duplicate values are automatically removed
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Create a set from a list
my_set2 = set([1, 2, 3, 4])  # Convert a list to a set
print(my_set2)  # Output: {1, 2, 3, 4}

# Create an empty set
my_set3 = {}  # This creates an empty dictionary, not an empty set
print(type(my_set3))  # Output: <class 'dict'>

# Create an empty set using the set() constructor
my_set4 = set()  # This creates an empty set
print(type(my_set4))  # Output: <class 'set'>