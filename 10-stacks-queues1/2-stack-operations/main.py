# Stack Operations - Python Example

stack = []

def push(val):
    stack.append(val)

def pop():
    if stack:
        return stack.pop()
    return None

def peek():
    if stack:
        return stack[-1]
    return None

def is_empty():
    return len(stack) == 0

push(1)
push(2)
print("Top element:", peek())
print("Pop element:", pop())
print("Is stack empty?", is_empty())
