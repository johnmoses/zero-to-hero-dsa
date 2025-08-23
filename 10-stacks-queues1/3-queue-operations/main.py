# Queue Operations - Python Example

from collections import deque

queue = deque()

def enqueue(val):
    queue.append(val)

def dequeue():
    if queue:
        return queue.popleft()
    return None

def front():
    if queue:
        return queue[0]
    return None

def is_empty():
    return len(queue) == 0

enqueue(1)
enqueue(2)
print("Front element:", front())
print("Dequeue element:", dequeue())
print("Is queue empty?", is_empty())
