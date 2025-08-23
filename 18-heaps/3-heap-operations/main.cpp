// Heap Operations - C++ Example

#include <iostream>
#include <vector>
#include <algorithm>

void heapify(std::vector<int>& arr, int n, int i) {
    int largest = i;
    int left = 2*i + 1;
    int right = 2*i + 2;

    if (left < n && arr[left] > arr[largest])
        largest = left;

    if (right < n && arr[right] > arr[largest])
        largest = right;

    if (largest != i) {
        std::swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}

void insert(std::vector<int>& heap, int val) {
    heap.push_back(val);
    int current = heap.size() - 1;
    while(current > 0) {
        int parent = (current - 1) / 2;
        if (heap[current] > heap[parent]) {
            std::swap(heap[current], heap[parent]);
            current = parent;
        } else {
            break;
        }
    }
}

int extractMax(std::vector<int>& heap) {
    if (heap.empty()) return -1;
    int maxVal = heap[0];
    heap = heap.back();
    heap.pop_back();
    heapify(heap, heap.size(), 0);
    return maxVal;
}

int main() {
    std::vector<int> heap;
    insert(heap, 3);
    insert(heap, 4);
    insert(heap, 9);
    insert(heap, 5);
    insert(heap, 2);

    std::cout << "Max heap array: ";
    for (int val : heap) std::cout << val << " ";
    std::cout << std::endl;

    int maxVal = extractMax(heap);
    std::cout << "Extract max: " << maxVal << std::endl;
    std::cout << "Heap after extraction: ";
    for (int val : heap) std::cout << val << " ";
    std::cout << std::endl;

    return 0;
}
