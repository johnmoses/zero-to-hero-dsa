""" 
Sets

Write a basic implementation of a set data structure with basic behaviours
"""
class Set:
    def __init__(self):
        self.data = []

    def add(self, value):
        if value not in self.data:
            self.data.append(value)

    def remove(self, value):
        if value in self.data:
            self.data.remove(value)

    def contains(self, value):
        return value in self.data

    def __str__(self):
        return str(self.data)

# Example usage
s = Set()
s.add(1)
s.add(2)
s.add(3)
s.add(3)
print(s)  # Output: [1, 2, 3]
s.remove(2)
print(s.contains(2))  # Output: False
print(s)  # Output: [1, 3]
