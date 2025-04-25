""" 
Queue implementation with deque library
"""

from collections import deque

class Queue:
    def __init__(self):
        self.values = deque()

    def __len__(self):
        return len(self.values)

    # Get size
    def getSize(self):
        return len(self.values)

    # Check if empty
    def isEmpty(self):
        return len(self.values) == 0

    # Get front or peek item
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.values[0]

    # binary number support method
    def front(self):
        return self.values[-1]

    # Insert an item
    def enqueue(self, val):
        self.values.append(val)
    
    # Remove an item
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.values.pop()

    def __str__(self):
        return str(self.values)

q = Queue()

q.enqueue('A')
q.enqueue('B')
q.enqueue('C')
print("Queue: ", q)
print("Size: ", q.getSize())
print("Dequeue: ", q.dequeue())
print("After dequeue: ", q)
print("Peek: ", q.peek())
print("Front: ", q.front())
print("isEmpty: ", q.isEmpty())
print("Size: ", q.getSize())