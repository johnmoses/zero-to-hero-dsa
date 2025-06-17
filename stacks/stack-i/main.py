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

class Stack1:
    def __init__(self):
        self.values = []

    def __str__(self):
        return str(self.values)
    
    def getSize(self):
        return len(self.values)

    def isEmpty(self):
        return len(self.values) == 0

    def top(self):
        self.values[-1]

    def push(self, val):
        self.values.append(val)

    def pop (self):
        return self.values.pop()

s = Stack1()
s.push('A')
s.push('B')
s.push('C')
print('Stack: ', s)
print('Size: ', s.getSize())
print('Pop: ', s.pop())
print('After pop: ', s)
print('Top: ', s.top())
print("isEmpty: ", s.isEmpty())
print('Size: ', s.getSize())