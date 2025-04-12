""" 
Write a basic example of bag data structure
"""
from collections import deque
from random import randint

class Bag:
    def __init__(self):
        self.bag = deque()

    def add(self, item):
        self.bag.append(item)

    def isEmpty(self):
        return len(self.bag) == 0

    def size(self):
        return len(self.bag)

    def __str__(self):
        return f"{self.bag}"

bag = Bag()
for i in range(10):
    bag.add(randint(1, 100))
print(bag)
print(bag.size())
print(bag.isEmpty())