""" 
Deque stack
"""

from collections import deque

class Stack:
    """
    Initialize a stack and add some behavious
    """
    def __init__(self):
        """
        Initialize a stack
        """
        self.values = deque()

    def __len__(self):
        """
        Get 
        return len(self.values)
        """

    def __str__(self):
        return str(self.values)

    def getSize(self):
        """
        Return the number of items in the stack
        Time Complexity: O(1)
        """
        return len(self.values)

    def isEmpty(self):
        """
        Check if the stack is empty
        Time Complexity: O(1)
        """
        return len(self.values)==0

    def peek(self):
        """
        Return the top item from the stack without removing it
        Time Complexity: O(1)
        Returns None if stack is empty
        """
        return self.values[-1]
    
    def push(self,val):
        """
        Add an item onto the top of the stack
        Time Complexity: O(1)
        """
        self.values.append(val)

    def pop(self):
        """
        Remove and return the top item from the stack
        Time Complexity: O(1)
        Returns None if stack is empty
        """
        return self.values.pop()

s = Stack()
s.push('A')
s.push('B')
s.push('C')
print('Stack: ', s)
print('Size: ', s.getSize())
print('Pop: ', s.pop())
print('After pop: ', s)
print('Peek: ', s.peek())
print("isEmpty: ", s.isEmpty())
print('Size: ', s.getSize())