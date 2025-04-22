""" 
Linked list implementation
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
    
    # Get size
    def getSize(self):
        return self.length
    
    # Check if empty
    def isEmpty(self):
        return self.length == 0
    
    # Get front or peek item
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.front.value
    
    # Insert an item or value
    def enqueue(self, val):
        node = Node(val)
        if self.rear is None:
            self.front = self.rear = node
            self.length += 1
            return
        self.rear.next = node
        self.rear = node
        self.length += 1
    
    # Remove an item
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        node = self.front
        self.front = node.next
        self.length -= 1
        if self.front is None:
            self.rear = None
        return node.value

    # Print queue
    def printQueue(self):
        node = self.front
        while node:
            print(node.value, end=" ")
            node = node.next
        print()

q = Queue()

q.enqueue('A')
q.enqueue('B')
q.enqueue('C')
q.printQueue()
print("Size: ", q.getSize())
print("Dequeue: ", q.dequeue())
print("Peek: ", q.peek())
print("isEmpty: ", q.isEmpty())
print("Size: ", q.getSize())
