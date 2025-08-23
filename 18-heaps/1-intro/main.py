# Heap Introduction - Python Example

import heapq

heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 3)
heapq.heappush(heap, 8)

print("Heap elements popped in order:")
while heap:
    print(heapq.heappop(heap))
