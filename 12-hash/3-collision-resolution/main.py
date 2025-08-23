# Collision Resolution - Python Example for Chaining

class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash(key)
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                self.buckets[index][i] = (key, value)
                return
        self.buckets[index].append((key, value))

    def get(self, key):
        index = self.hash(key)
        for k, v in self.buckets[index]:
            if k == key:
                return v
        return None

hmap = HashMap()
hmap.insert("apple", 3)
hmap.insert("banana", 5)
print("Apple count:", hmap.get("apple"))
