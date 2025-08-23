// Queue Operations - C++ Example

#include <iostream>
#include <queue>

int main() {
    std::queue<int> queue;

    queue.push(1);
    queue.push(2);

    if (!queue.empty())
        std::cout << "Front element: " << queue.front() << std::endl;

    if (!queue.empty()) {
        std::cout << "Dequeue element: " << queue.front() << std::endl;
        queue.pop();
    }

    std::cout << "Is queue empty? " << (queue.empty() ? "Yes" : "No") << std::endl;

    return 0;
}
