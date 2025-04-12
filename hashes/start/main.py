""" 
Hashes

Write a basic implementation of hash map with a hash function.
Give step by step explanations.
"""
class HashMap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * capacity
        self.size = 0

    def hash_function(self, key):
        """
        A simple hash function that uses the built-in hash() function and modulo operator.
        """
        return hash(key) % self.capacity

    def insert(self, key, value):
        """
        Inserts a key-value pair into the hash map.
        Handles collisions using separate chaining.
        """
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            self.table[index].append((key, value))
        self.size += 1

    def get(self, key):
        """
        Retrieves the value associated with the given key.
        Returns None if the key is not found.
        """
        index = self.hash_function(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None

    def delete(self, key):
        """
        Deletes the key-value pair associated with the given key.
        Returns True if the key was found and deleted, False otherwise.
        """
        index = self.hash_function(key)
        if self.table[index] is not None:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    del self.table[index][i]
                    self.size -= 1
                    return True
        return False

    def __len__(self):
        """
        Returns the number of key-value pairs in the hash map.
        """
        return self.size

    def __str__(self):
        return str(self.table)

hmap = HashMap(2)
hmap.insert(1,'A')
hmap.insert(2,'B')
print(hmap)