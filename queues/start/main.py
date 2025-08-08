"""
Write a basic array queue data structure showing basic functionalities
"""

queue = []

# Enqueue or insert item at the back
queue.append('A')
queue.append('B')
queue.append('C')
print("Queue: ", queue)

# isEmpty
isEmpty = not bool(queue)
print("isEmpty: ", isEmpty)

# Alternatively 
print("isEmpty: ", len(queue) == 0)

# Size
print("Size: ", len(queue))

# Dequeue or remove item from front
element = queue.pop(0)
print("Dequeue: ", element)
print("After deueue: ", queue)

# Peek or get value of front item
frontElement = queue[0]
print("Peek: ", frontElement)
