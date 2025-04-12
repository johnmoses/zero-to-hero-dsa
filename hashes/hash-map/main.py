"""
Hash Map
"""

class HashMap:
    def __init__(self):
        self.hm = {}

    def put(self, key: int, val: int) -> None:
        self.hm[key] = val

    def get(self, key: int) -> int:
        return self.hm[key] if key in self.hm else -1

    def remove(self, key: int) -> None:
        if key in self.hm:
            del self.hm[key]

    def __str__(self):
        return str(self.hm)

hm = HashMap()
hm.put(1,'A')
hm.put(2,'B')
hm.put(3, 'C')
param_1 = hm.get(1)
hm.remove(1)
print(param_1)
print(hm)