""" 
Class example of queue
"""

class Queue:
    """ 
    Initialize a queue and add some behavious
    """
    # The constructor
    def __init__(self):
        self.values = []

    # Acessor function
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
    
    # Insert an item at the back
    def enqueue(self, val):
        self.values.append(val)
    
    # Remove an item from the front
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.values.pop(0)

    def __str__(self):
        return str(self.values)


q = Queue()

q.enqueue('A')
q.enqueue('B')
q.enqueue('C')
print("Queue: ", q)
print("Size: ", q.getSize())
print("Dequeue: ", q.dequeue())
print("After deueue: ", q)
# print("Peek: ", q.peek())
# print("isEmpty: ", q.isEmpty())
print("Size: ", q.getSize())
