# Min and Max Heap - Python Example

import heapq

min_heap = []
max_heap = []

for num in [5, 3, 8, 1]:
    heapq.heappush(min_heap, num)
    heapq.heappush(max_heap, -num)  # invert for max heap

print("Min heap order:")
while min_heap:
    print(heapq.heappop(min_heap))

print("Max heap order:")
while max_heap:
    print(-heapq.heappop(max_heap))
