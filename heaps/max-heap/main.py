""" 
Max heap.
"""
import heapq

# Initialize empty heaps
max_heap = []

#we want to store 10, but change it to -10 for max-heap
heapq.heappush(max_heap, -10)
print(max_heap)

#we want to store 7, but change it to -7 for max-heap
heapq.heappush(max_heap, -7)
print(max_heap)

max_element_from_heap = -1 * heapq.heappop(max_heap)
print(max_element_from_heap)
print(max_heap)
#heap = [-7], -10 is removed
#max_element_from_heap = 10, we have retrieved the largest element from the heap