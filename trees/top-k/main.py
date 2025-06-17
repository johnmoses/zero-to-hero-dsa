""" 
Find the k-th largest element in an unsorted array.

Example:
Input: nums = [3, 2, 1, 5, 6, 4], k = 2
Output: 5

Explanation:
Use a min-heap of size k to keep track of the k largest elements.
Iterate through the array, adding elements to the heap.
If the heap size exceeds k, remove the smallest element from the heap.
The root of the heap will be the k-th largest element.
"""
from heapq import heappush, heappop, nlargest

def findKthLargest1(heap: list[int], k: int) -> int:
    return nlargest(k, heap)[-1]

def findKthLargest2(nums: list[int], k: int) -> int:
    # Use min heap to track k largest elements
    heap = []
    
    for num in nums:
        heappush(heap, num)
        if len(heap) > k:
            heappop(heap)
            
    # Root is kth largest element
    return heap[0]

print(findKthLargest1([3, 2, 1, 5, 6, 4], 2))
print(findKthLargest2([3, 2, 1, 5, 6, 4], 2))