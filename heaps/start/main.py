""" 
Heap data structure

Write a script to demonstrate heap data structure.
"""
import heapq

# Initialize empty heaps, one for integers and one for tuples
heap1 = []
heap2 = []

# Add elements to the heap 1
heapq.heappush(heap1, 7)
heapq.heappush(heap1, 5)
heapq.heappush(heap1, 10)

print(heap1)

# Add elements to the heap 2
heapq.heappush(heap2, (5, 'write code'))
heapq.heappush(heap2, (7, 'release product'))
heapq.heappush(heap2, (1, 'write spec'))
heapq.heappush(heap2, (3, 'create tests'))

# Print heap 2
print(heap2)

# Remove elements from the heap
print(heapq.heappop(heap2))
print(heapq.heappop(heap2))
print(heapq.heappop(heap2))