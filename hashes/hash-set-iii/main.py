"""
Hash Set example
"""

# ["HashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
# [[], [1], [2], [1], [3], [2], [2], [2], [2]]

class HashSet:

    def __init__(self):
        # data structure
        self.table = [0] * 20

    def add(self, key: int) -> None:
        self.table[key] = 1

    def remove(self, key: int) -> None:
        self.table[key] = 0

    def contains(self, key: int) -> bool:
        # Return true if it has the element
        return self.table[key]

    def __str__(self):
        res = f"{self.table}"
        return res

obj = HashSet()
print(obj)
obj.add(1)
print(obj.contains(1))
# Output [null, null, null, true, false, null, true, null, false]