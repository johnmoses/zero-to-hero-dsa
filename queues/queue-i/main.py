""" 
Class example of queue
"""

class Queue:
    """ 
    Initialize a queue and add some behavious
    """
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)
    
    # Get size
    def getSize(self):
        return len(self.data)
    
    # Check if empty
    def isEmpty(self):
        return len(self.data) == 0
    
    # Get front or peek item
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.data[0]
    
    # Insert an item
    def enqueue(self, val):
        self.data.append(val)
    
    # Remove an item
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.data.pop(0)

    def __str__(self):
        return str(self.data)


q = Queue()

q.enqueue('A')
q.enqueue('B')
q.enqueue('C')
print("Queue: ", q.data)
print("Size: ", q.getSize())
print("Dequeue: ", q.dequeue())
print("Peek: ", q.peek())
print("isEmpty: ", q.isEmpty())
print("Size: ", q.getSize())
print(q)