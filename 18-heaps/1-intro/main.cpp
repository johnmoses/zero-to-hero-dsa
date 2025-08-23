// Heap Introduction - C++ Example

#include <iostream>
#include <queue>
#include <vector>

int main() {
    std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap;
    minHeap.push(5);
    minHeap.push(3);
    minHeap.push(8);

    std::cout << "Heap elements popped in order:" << std::endl;
    while (!minHeap.empty()) {
        std::cout << minHeap.top() << std::endl;
        minHeap.pop();
    }
    return 0;
}
