"""
Array Stack
"""

class Stack:
    """ 
    Initialize a stack and add some behavious
    """
    def __init__(self):
        self.values = []

    def __len__(self):
        return len(self.values)

    # Get size
    def getSize(self):
        return len(self.values)

    # Check if empty
    def isEmpty(self):
        return len(self.values) == 0

    # Get top or peek item
    def top(self):
        return self.values[-1]

    # Insert an item
    def push(self, val):
        self.values.append(val)

    # Remove an item from top
    def pop(self):
        return self.values.pop()

    def __str__(self):
        return str(self.values)

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print('Stack: ', s.values)
print('Size: ', s.getSize())
print('Pop: ', s.pop())
print('Top: ', s.top())
print("isEmpty: ", s.isEmpty())
print('Size: ', s.getSize())
print(s)