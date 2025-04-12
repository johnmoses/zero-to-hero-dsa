""" 
Heap data structure

Write a script to demonstrate heap data structure.
"""
import heapq

h = []
heapq.heappush(h, (5, 'write code'))
heapq.heappush(h, (7, 'release product'))
heapq.heappush(h, (1, 'write spec'))
heapq.heappush(h, (3, 'create tests'))
print(heapq.heappop(h))
print(heapq.heappop(h))
print(heapq.heappop(h))