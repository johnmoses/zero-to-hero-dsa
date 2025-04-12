""" 
Linked list stack
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    
    # Get size
    def getSize(self):
        return self.size

    # Check if empty
    def isEmpty(self):
        return self.size == 0
    
    # Get top or peek item
    def top(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.head.data
    
    # Insert an item
    def push(self, val):
        node = Node(val)
        if self.head:
            node.next = self.head
        self.head = node
        self.size += 1
    
    # Remove an item
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        node = self.head
        self.head = self.head.next
        self.size -= 1
        return node.data

    # Print stack
    def printStack(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.printStack()
print('Size: ', s.getSize())
print('Pop: ', s.pop())
print('Top: ', s.top())
print("isEmpty: ", s.isEmpty())
print('Size: ', s.getSize())