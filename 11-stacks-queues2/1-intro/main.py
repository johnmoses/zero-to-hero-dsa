# Advanced Stacks and Queues - Python Example

from collections import deque

# Demonstration of deque operations
dq = deque()
dq.append(1)       # add to right
dq.appendleft(2)   # add to left
print(dq)          # deque([2,1])

dq.pop()           # remove from right
dq.popleft()       # remove from left
print(dq)          # deque([])
