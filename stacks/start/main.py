"""
Stacks

Given some items, A, B, C, and so on, write a basic stack datastructure to demonstrate it's core functionality
"""

stack = []

# Push or insert item at the top
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack: ", stack)

# Check if empty stack
print("isEmpty: ", len(stack) == 0)

# Get size
print("Size: ", len(stack))

# Pop or remove an item (last) from top
print("Pop: ", stack.pop())
print("After pop: ", stack)

# Get peek or top (last) item
print("Peek: ", stack[-1])
