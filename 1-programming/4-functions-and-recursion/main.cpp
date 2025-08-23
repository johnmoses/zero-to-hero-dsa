// 4 Functions And Recursion - C++ example

#include <iostream>

void greet(std::string name) {
    std::cout << "Hello, " << name << std::endl;
}

int factorial(int n) {
    if (n == 0) return 1;
    else return n * factorial(n - 1);
}

int main() {
    greet("Alice");
    std::cout << "Factorial of 5: " << factorial(5) << std::endl;
    return 0;
}
