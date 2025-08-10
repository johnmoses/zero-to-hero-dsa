"""
Array Stack
"""

class Stack:
    """ 
    Initialize a stack and add some behavious
    """
    def __init__(self):
        """
        Initialize a stack
        """
        self.values = []

    def __len__(self):
        """
        Get the length of the stack
        """
        return len(self.values)

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
        return len(self.values) == 0

    def peek(self):
        """
        Return the top item from the stack without removing it
        Time Complexity: O(1)
        Returns None if stack is empty
        """
        if self.isEmpty():
            raise IndexError("peek from empty stack")
        return self.values[-1]

    def push(self, val):
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
        if self.isEmpty():
            raise IndexError("pop from empty stack")
        return self.values.pop()

    def clear(self):
        """
        Remove all items from the stack
        Time Complexity: O(1)
        """
        self.values = []

    def __str__(self):
        """
        Get the string representation of the stack
        """
        return str(self.values)


s = Stack()
s.push('A')
s.push('B')
s.push('C')
s.push(1)
s.push(2)
s.push(3)

print('Stack: ', s)
print('Size: ', s.getSize())
print('Pop: ', s.pop())
print('After pop: ', s)
print('Top: ', s.peek())
print("isEmpty: ", s.isEmpty())
print('Size: ', s.getSize())

s.clear()
print('After clear: ', s)
print('Size: ', s.getSize())