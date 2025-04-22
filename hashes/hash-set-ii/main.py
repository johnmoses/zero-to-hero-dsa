
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
        self.size = 10
        self.values = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def add(self, key):
        index = self._hash(key)
        if key not in self.values[index]:
            self.values[index].append(key)

    def contains(self, key):
        index = self._hash(key)
        return key in self.values[index]

    def remove(self, key):
        index = self._hash(key)
        if key in self.values[index]:
            self.values[index].remove(key)

    def print_set(self):
        print(self.values)
        for i in range(len(self.values)):
            print(f"Index {i}: {self.values[i]}")
            for j in range(len(self.values[i])):
                print(f"  Item {j}: {self.values[i][j]}")
                print(f"    Hash: {self._hash(self.values[i][j])}")
                print(f"    Index: {self._hash(self.values[i][j]) % self.size}")
                print(f"    Key: {self.values[i][j]}")
                print(f"    Value: {self.values[i][j]}")
                print(f"    Hash: {self._hash(self.values[i][j])}")
                print(f"    Index: {self._hash(self.values[i][j]) % self.size}")

hash_set = HashSet()
hash_set.add(1)
hash_set.add(2)
print(hash_set.contains(1))
print(hash_set.contains(3))
hash_set.add(2)
print(hash_set.contains(2))
hash_set.remove(2)
hash_set.print_set()
hash_set.add(3)
print(hash_set.contains(2))
hash_set.print_set()