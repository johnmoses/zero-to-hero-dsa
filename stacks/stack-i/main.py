"""
Array Stack
"""

class Stack:
    """ 
    Initialize a stack and add some behavious
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

    # Get top or peek item
    def top(self):
        return self.data[-1]

    # Insert an item
    def push(self, val):
        self.data.append(val)

    # Remove an item from top
    def pop(self):
        return self.data.pop()

    def __str__(self):
        return str(self.data)

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print('Stack: ', s.data)
print('Size: ', s.getSize())
print('Pop: ', s.pop())
print('Top: ', s.top())
print("isEmpty: ", s.isEmpty())
print('Size: ', s.getSize())
print(s)