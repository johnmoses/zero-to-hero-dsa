""" 
Linked list stack
"""

class Node:
    def __init__(self, value):
        self.value = value
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
        return self.head.value
    
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
        return node.value

    # Print stack
    def printStack(self):
        temp = self.head
        while temp:
            print(temp.value, end=" ")
            temp = temp.next
        print()

s = Stack()
s.push('A')
s.push('B')
s.push('C')
s.printStack()
print('Size: ', s.getSize())
print('Pop: ', s.pop())
print('Top: ', s.top())
print("isEmpty: ", s.isEmpty())
print('Size: ', s.getSize())