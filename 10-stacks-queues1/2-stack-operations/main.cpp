// Stack Operations - C++ Example

#include <iostream>
#include <stack>

int main() {
    std::stack<int> stack;

    stack.push(1);
    stack.push(2);

    if (!stack.empty())
        std::cout << "Top element: " << stack.top() << std::endl;

    if (!stack.empty()) {
        std::cout << "Pop element: " << stack.top() << std::endl;
        stack.pop();
    }

    std::cout << "Is stack empty? " << (stack.empty() ? "Yes" : "No") << std::endl;

    return 0;
}
