# Stack and Queue Introduction - Python Example

stack = []
stack.append(1)
stack.append(2)
print("Stack pop:", stack.pop())

from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
print("Queue pop:", queue.popleft())
