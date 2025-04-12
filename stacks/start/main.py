"""
Stacks

Given some items, A, B, C, and so on, write a basic stack datastructure to demonstrate it's core functionality
"""

stack = []

# Push
stack.append('A')
stack.append('B')
stack.append('C')

print("Stack: ", stack)

# Push or insert an item
print("Push: ", stack.append('D'))
print("Stack: ", stack)

# Pop or remove an item
print("Pop: ", stack.pop())
print("Stack: ", stack)

# Get peek or top item
print("Peek: ", stack[-1])

# Check if empty stack
print("isEmpty: ", len(stack) == 0)

# Get size
print("Size: ", len(stack))