"""
Hash Sets
"""
# create a hash with set keyword
hashset = set()

# add a key
hashset.add(1)
hashset.add(2)
hashset.add(3)

# Show the size
print("Size is ", len(hashset))

# Remove a key
hashset.remove(3)
print("Size is ", len(hashset))

# check for a key
if ( 2 not in hashset):
    print('2 not in hash set')

# Iterate 
for x in hashset:
    print(x, end=" ")
print("Iterated ", len(hashset))

# Clear hash set
hashset.clear()
print("Size is ", len(hashset))