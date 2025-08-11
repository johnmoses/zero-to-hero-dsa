""" 
Linked List Queue
"""
class Node:
    """
    Node
    """
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    """
    Initialize queue and add some behavious
    """
    def __init__(self):
        """
        Initialize queue
        """
        self.front = None
        self.rear = None
        self.size = 0

    def getSize(self):
        """
        Return size of the queue
        """
        return self.size

    def isEmpty(self):
        """
        Check if the queue is empty
        """
        return self.size == 0

    def push(self, value):
        """
        Add a value to the queue
        """
        new_node = Node(value)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
        self.size += 1

    def pop(self):
        """
        Remove a value from the queue
        """
        if self.front is None:
            return None
        temp = self.front
        self.front = temp.next
        self.size -= 1
        if self.front is None:
            self.rear = None
        return temp.value

    def display(self):
        """
        Display queue
        """
        current = self.front
        while current:
            print(current.value, end=" ")
            current = current.next
        print()

q = Queue()
q.push('A')
q.push('B')
q.push('C')
q.display()
print('Size: ', q.getSize())
print("Pop item is", q.pop())
q.display()
print("isEmpty: ", q.isEmpty())
print('Size: ', q.getSize())
