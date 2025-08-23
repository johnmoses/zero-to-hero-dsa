// main.cpp
// C++ example code demonstrating basic programming concepts.

#include <iostream>

// Function to print Hello World
void helloWorld() {
    std::cout << "Hello, World!" << std::endl;
}

// Function to add two numbers
int addNumbers(int a, int b) {
    return a + b;
}

// Recursive factorial function
int factorial(int n) {
    if (n == 0) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

int main() {
    helloWorld();
    std::cout << "Sum of 3 and 5: " << addNumbers(3, 5) << std::endl;
    std::cout << "Factorial of 5: " << factorial(5) << std::endl;
    return 0;
}
