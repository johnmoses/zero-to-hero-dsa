# Top K Elements - Python Example

import heapq

def find_top_k_elements(arr, k):
    if k <= 0:
        return []
    min_heap = []
    for num in arr:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        elif num > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)
    return min_heap

# Example usage
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
k = 3
result = find_top_k_elements(arr, k)
print(f"Top {k} elements are: {result}")
