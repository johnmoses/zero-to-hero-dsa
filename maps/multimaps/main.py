""" 
Multisets

Write a basic implementation of a multiset data structure with basic behaviours
"""
class MultiSet:
    def __init__(self):
        self.data = []

    def add(self, value):
        self.data.append(value)

    def remove(self, value):
        if value in self.data:
            self.data.remove(value)

    def contains(self, value):
        return value in self.data

    def __str__(self):
        return str(self.data)

# Example usage
ms = MultiSet()
ms.add(1)
ms.add(2)
ms.add(3)
ms.add(3)
print(ms)  # Output: [1, 2, 3]
ms.remove(2)
print(ms.contains(2))  # Output: False
print(ms)  # Output: [1, 3]