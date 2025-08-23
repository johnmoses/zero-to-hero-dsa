// Min and Max Heap - C++ Example

#include <iostream>
#include <queue>
#include <vector>

int main() {
    std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap;
    std::priority_queue<int> maxHeap;

    int nums[] = {5, 3, 8, 1};
    for (int num : nums) {
        minHeap.push(num);
        maxHeap.push(num);
    }

    std::cout << "Min heap order:" << std::endl;
    while (!minHeap.empty()) {
        std::cout << minHeap.top() << std::endl;
        minHeap.pop();
    }

    std::cout << "Max heap order:" << std::endl;
    while (!maxHeap.empty()) {
        std::cout << maxHeap.top() << std::endl;
        maxHeap.pop();
    }
    return 0;
}
