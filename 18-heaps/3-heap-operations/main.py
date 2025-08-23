# Heap Operations - Python Example

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def insert(heap, val):
    heap.append(val)
    current = len(heap) - 1

    while current > 0:
        parent = (current - 1) // 2
        if heap[current] > heap[parent]:
            heap[current], heap[parent] = heap[parent], heap[current]
            current = parent
        else:
            break

def extract_max(heap):
    if not heap:
        return None
    max_val = heap[0]
    heap = heap.pop()
    heapify(heap, len(heap), 0)
    return max_val

# Usage example
heap = []
insert(heap, 3)
insert(heap, 4)
insert(heap, 9)
insert(heap, 5)
insert(heap, 2)

print("Max heap array:", heap)
print("Extract max:", extract_max(heap))
print("Heap after extraction:", heap)
