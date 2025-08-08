""" 
Hashes

Design a hash map with ability to insert, access and delete items.

Example 1:
    Input
    ["HashMap", "insert", "insert", "get", "get", "insert", "get", "delete", "get"]
    [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
    Output
    [null, null, null, 1, -1, null, 1, null, -1]

Constraints:
0 <= key, value <= 106
At most 104 calls will be made to put, get, and remove.
"""
class HashMap:
    def __init__(self):
        # Initialize fixed size array with None values
        self.size = 10
        self.values = [[] for _ in range(self.size)]

    def __str__(self):
        return str(self.values)

    
    def _hash(self, key):
        # Simple hash function that maps key to index
        return key % self.size

        
    def add(self, key, value):
        # Get hash of key
        index = self._hash(key)
        
        # Check if key exists and update value
        for item in self.values[index]:
            if item[0] == key:
                item[1] = value
                return
                
        # Insert new key-value pair
                
        self.values[index].append([key, value])

        
    def get(self, key):
        # Get hash of key
        index = self._hash(key)
        
        # Return value if key found, else -1
        for item in self.values[index]:
            if item[0] == key:
                return item[1]
        return -1
        
    def remove(self, key):
        # Get hash of key 
        index = self._hash(key)
        
        # Remove item if key found
        for i, item in enumerate(self.values[index]):
            if item[0] == key:
                self.values[index].pop(i)
                return
                
    def print_map(self):
        print(self.values)


hm = HashMap()
hm.add(1, 1)
hm.add(2, 2)
print(hm.get(1))  # Output: 1
print(hm.get(3))  # Output: -1
hm.add(2, 1)
print(hm.get(2))  # Output: 1
hm.remove(2)
hm.add(3, 3)
print(hm.get(2))  # Output: -1
hm.print_map()
print(hm)
