// Stack and Queue Introduction - C++ Example

#include <iostream>
#include <stack>
#include <queue>

int main() {
    std::stack<int> stack;
    stack.push(1);
    stack.push(2);
    std::cout << "Stack pop: " << stack.top() << std::endl;
    stack.pop();

    std::queue<int> queue;
    queue.push(1);
    queue.push(2);
    std::cout << "Queue pop: " << queue.front() << std::endl;
    queue.pop();

    return 0;
}
