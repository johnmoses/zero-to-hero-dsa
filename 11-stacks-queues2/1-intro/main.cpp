// Advanced Stacks and Queues - C++ Example

#include <iostream>
#include <deque>

int main() {
    std::deque<int> dq;
    dq.push_back(1);       // add to right
    dq.push_front(2);      // add to left

    for (int val : dq) std::cout << val << " "; // prints: 2 1
    std::cout << std::endl;

    dq.pop_back();         // remove from right
    dq.pop_front();        // remove from left

    std::cout << "Size after pops: " << dq.size() << std::endl; // 0
    return 0;
}
