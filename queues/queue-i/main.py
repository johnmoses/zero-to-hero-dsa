""" 
Class example of queue
"""

class Queue:
    """ 
    Initialize a queue and add some behavious
    """
    def __init__(self):
        """
        Initialize a queue
        """
        self.values = []

    def isEmpty(self):
        """
        Check if the queue is empty
        """
        return len(self.values) == 0

    def size(self):
        """
        Return the size of the queue
        """
        return len(self.values)

    def push(self, value):
        """
        Add a value to the queue
        """
        self.values.append(value)

    def pop(self):
        """
        Remove a value from the queue
        """
        if self.isEmpty():
            raise Exception("Queue is empty")
        return self.values.pop(0)

    def peek(self):
        """
        Return the first or front value in the queue
        """
        if self.isEmpty():
            raise Exception("Queue is empty")
        return self.values[0]
    
    def back(self):
        """
        Return the last value in the queue
        """
        return self.values[-1]

    def clear(self):
        """
        Clear the queue
        """
        self.values = []

    def __len__(self):
        """
        Return the size of the queue
        """
        return len(self.values)

    def __str__(self):
        """
        Return the queue as a string
        """
        return str(self.values)


q = Queue()

q.push('A')
q.push('B')
q.push('C')
q.push(1)
q.push(2)
q.push(3)
print("Queue: ", q)
print("Size: ", q.size())
print("Pop: ", q.pop())
print("After pop: ", q)
print("Peek: ", q.peek())
print("Back: ", q.back())
print("isEmpty: ", q.isEmpty())
print("Size: ", q.size())
q.clear()
print("After clear: ", q)
print("isEmpty: ", q.isEmpty())
