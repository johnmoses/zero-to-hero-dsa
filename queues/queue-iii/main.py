""" 
Linked List Queue
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    # Get size
    def getSize(self):
        return self.size

    # Check if empty
    def isEmpty(self):
        return self.size == 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.front is None:
            return None
        temp = self.front
        self.front = temp.next
        self.size -= 1
        if self.front is None:
            self.rear = None
        return temp.value

    def display(self):
        current = self.front
        while current:
            print(current.value, end=" ")
            current = current.next
        print()

q = Queue()
q.enqueue('A')
q.enqueue('B')
q.enqueue('C')
q.display()
print('Size: ', q.getSize())
print("Dequeued item is", q.dequeue())
q.display()
print("isEmpty: ", q.isEmpty())
print('Size: ', q.getSize())
