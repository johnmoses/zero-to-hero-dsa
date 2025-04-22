"""
Hash Map
"""

class HashMap:
    def __init__(self):
        self.values = []

    def add(self, key, value):
        for item in self.values:
            if item[0] == key:
                item[1] = value
                return
        self.values.append([key, value])

    def get(self, key):
        for item in self.values:
            if item[0] == key:
                return item[1]
        return None

    def has(self, key):
        for item in self.values:
            if item[0] == key:
                return True
        return False

    def remove(self, key):
        for i, item in enumerate(self.values):
            if item[0] == key:
                del self.values[i]
                return True
        return False

    def __str__(self):
        return str(self.values)
        

hm = HashMap()
hm.add(1,'A')
hm.add(2,'B')
hm.add(3, 'C')
param_1 = hm.get(1)
hm.remove(1)
print(param_1)
print(hm)