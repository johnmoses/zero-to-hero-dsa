""" 
Queue implementation with deque library
"""

from collections import deque

class Queue:
    """
    Initialize queue and add some behavious
    """
    def __init__(self):
        """
        Initialize queue
        """
        self.values = deque()

    def __len__(self):
        """
        Lenght of queues
        """
        return len(self.values)

    def isEmpty(self):
            """
            Check if empty
            """
            return len(self.values) == 0

    def getSize(self):
        """
        Return the size of the queue
        """
        return len(self.values)

    def push(self, val):
        """
        Add value to the queue
        """
        self.values.append(val)
    
    def pop(self):
        """
        Remove a value from queue
        """
        if self.isEmpty():
            return "Queue is empty"
        return self.values.pop()
    
    def peek(self):
        """
        Return the first value in the queue
        """
        if self.isEmpty():
            return "Queue is empty"
        return self.values[0]

    def back(self):
        """
        Return the last value in the queue
        """
        return self.values[-1]

    def __str__(self):
        """
        Return the queue as a string
        """
        return str(self.values)

q = Queue()

q.push('A')
q.push('B')
q.push('C')
print("Push: ", q)
print("Size: ", q.getSize())
print("Pop: ", q.pop())
print("After pop: ", q)
print("Peek: ", q.peek())
print("Back: ", q.back())
print("isEmpty: ", q.isEmpty())
print("Size: ", q.getSize())