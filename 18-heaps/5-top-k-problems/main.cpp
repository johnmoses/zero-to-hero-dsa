// Top K Elements - C++ Example

#include <iostream>
#include <vector>
#include <queue>

std::vector<int> findTopKElements(const std::vector<int>& arr, int k) {
    if (k <= 0) return {};
    std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap;
    for (int num : arr) {
        if (minHeap.size() < k) {
            minHeap.push(num);
        } else if (num > minHeap.top()) {
            minHeap.pop();
            minHeap.push(num);
        }
    }
    std::vector<int> result;
    while (!minHeap.empty()) {
        result.push_back(minHeap.top());
        minHeap.pop();
    }
    return result;
}

int main() {
    std::vector<int> arr = {3,1,4,1,5,9,2,6,5};
    int k = 3;
    std::vector<int> topK = findTopKElements(arr, k);
    std::cout << "Top " << k << " elements are: ";
    for (int val : topK) std::cout << val << " ";
    std::cout << std::endl;
    return 0;
}
