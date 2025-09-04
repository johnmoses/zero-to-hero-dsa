""" 
Linked list stack
"""

class Node:
    """
    Initialize Node
    """
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    """ 
    Initialize a stack and add some behavious
    """
    def __init__(self):
        self.head = None
        self.size = 0
    
    def getSize(self):
        """
        Return the number of items in the stack
        Time Complexity: O(1)
        """
        return self.size

    def isEmpty(self):
        """
        Check if the stack is empty
        Time Complexity: O(1)
        """
        return self.size == 0
    
    def peek(self):
        """
        Return the top item
        """
        if self.isEmpty():
            return "Stack is empty"
        return self.head.value
    
    def push(self, val):
        """
        Insert item
        """
        node = Node(val)
        if self.head:
            node.next = self.head
        self.head = node
        self.size += 1
    
    def pop(self):
        """
        Remove item
        """
        if self.isEmpty():
            return "Stack is empty"
        node = self.head
        self.head = self.head.next
        self.size -= 1
        return node.value

    def printStack(self):
        """
        Print stack
        """
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
print('Peek: ', s.peek())
print("isEmpty: ", s.isEmpty())
print('Size: ', s.getSize())