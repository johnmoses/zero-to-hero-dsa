""" 
Write a basic example of set data structure with basic functionalities
"""
# Creating a set
st = {1, 2, 3, 4, 5}
print("Original set:", st)

# Adding elements to the set
st.add(6)
print("After adding 6:", st)
st.update([7, 8, 9])
print("After updating with [7, 8, 9]:", st)

# Removing elements from the set
st.remove(3)
print("After removing 3:", st)
st.discard(8)
print("After discarding 8:", st)

# Checking if an element is in the set
print("Is 4 in the set?", 4 in st)
print("Is 10 in the set?", 10 in st)

# Create a set from a list
st1 = set([1, 2, 3, 4])  # Convert a list to a set
print(st1)  # Output: {1, 2, 3, 4}

# Create an empty set
st2 = {}  # This creates an empty dictionary, not an empty set
print(type(st2))  # Output: <class 'dict'>

# Create an empty set using the set() constructor
st3 = set()  # This creates an empty set
print(type(st3))  # Output: <class 'set'>

# More set operations
st4 = {1, 2, 3, 4, 5}
st5 = {4, 5, 6, 7, 8}
print("Union:", st4.union(st5))
print("Intersection:", st4.intersection(st5))
print("Difference:", st4.difference(st5))
print("Symmetric difference:", st4.symmetric_difference(st5))
