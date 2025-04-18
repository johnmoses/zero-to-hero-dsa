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
        self.size = 100
        self.table = [[] for _ in range(self.size)]

    
    def _hash(self, key):
        # Simple hash function that maps key to index
        return key % self.size

        
    def insert(self, key, value):
        # Get hash of key
        index = self._hash(key)
        
        # Check if key exists and update value
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
                
        # Insert new key-value pair
                
        self.table[index].append([key, value])

        
    def get(self, key):
        # Get hash of key
        index = self._hash(key)
        
        # Return value if key found, else -1
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return -1
        
    def delete(self, key):
        # Get hash of key 
        index = self._hash(key)
        
        # Remove item if key found
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                self.table[index].pop(i)
                return
                # del self.table[index][i]
                # return
                
    def print_table(self):
        print(self.table)

hash_map = HashMap()
hash_map.insert(1, 1)
hash_map.insert(2, 2)
print(hash_map.get(1))  # Output: 1
print(hash_map.get(3))  # Output: -1
hash_map.insert(2, 1)
print(hash_map.get(2))  # Output: 1
hash_map.delete(2)
hash_map.insert(3, 3)
print(hash_map.get(2))  # Output: -1
hash_map.print_table()

""" 
Design a hash set with insert, contains and delete behaviours.

Example 1:
    ["HashSet", "insert", "insert", "contains", "contains", "insert", "contains", "delete", "contains"]
    [[], [1], [2], [1], [3], [2], [2], [2], [2]]
    Output
    [null, null, null, true, false, nul

Constraints:
0 <= key <= 106
At most 104 calls will be made to insert, delete, and contains.
"""
class HashSet:
    def __init__(self):
        self.size = 100
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def insert(self, key):
        index = self._hash(key)
        if key not in self.table[index]:
            self.table[index].append(key)

    def contains(self, key):
        index = self._hash(key)
        return key in self.table[index]

    def delete(self, key):
        index = self._hash(key)
        if key in self.table[index]:
            self.table[index].remove(key)

    def print_table(self):
        print(self.table)
        for i in range(len(self.table)):
            print(f"Index {i}: {self.table[i]}")
            for j in range(len(self.table[i])):
                print(f"  Item {j}: {self.table[i][j]}")
                print(f"    Hash: {self._hash(self.table[i][j])}")
                print(f"    Index: {self._hash(self.table[i][j]) % self.size}")
                print(f"    Key: {self.table[i][j]}")
                print(f"    Value: {self.table[i][j]}")
                print(f"    Hash: {self._hash(self.table[i][j])}")
                print(f"    Index: {self._hash(self.table[i][j]) % self.size}")

hash_set = HashSet()
hash_set.insert(1)
hash_set.insert(2)
print(hash_set.contains(1))
print(hash_set.contains(3))
hash_set.insert(2)
print(hash_set.contains(2))
hash_set.delete(2)
hash_set.print_table()
hash_set.insert(3)
print(hash_set.contains(2))
hash_set.print_table()