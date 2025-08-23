// Expression Evaluation - C++ Example

#include <iostream>
#include <stack>
#include <sstream>
#include <string>
#include <cctype>
#include <cmath>

int evaluatePostfix(const std::string& expr) {
    std::stack<int> stack;
    std::istringstream iss(expr);
    std::string token;

    while (iss >> token) {
        if (isdigit(token[0])) {
            stack.push(std::stoi(token));
        } else {
            int b = stack.top(); stack.pop();
            int a = stack.top(); stack.pop();

            if (token == "+") stack.push(a + b);
            else if (token == "-") stack.push(a - b);
            else if (token == "*") stack.push(a * b);
            else if (token == "/") stack.push(a / b);
            // Skipping ^ operator example for brevity
        }
    }
    return stack.top();
}

int main() {
    std::string expr = "3 4 2 * 1 5 - 2 3 ^ ^ / +";
    std::cout << "Result of postfix expression: " << evaluatePostfix(expr) << std::endl;
    return 0;
}
