""" 
Write a basic example of bag data structure
"""
from collections import deque
from random import randint

class Bag:
    def __init__(self):
        self.values = deque()

    def add(self, value):
        self.values.append(value)

    def isEmpty(self):
        return len(self.values) == 0

    def size(self):
        return len(self.values)

    def __str__(self):
        return f"{self.values}"

bag = Bag()
for i in range(10):
    bag.add(randint(1, 100))
print(bag)
print(bag.size())
print(bag.isEmpty())