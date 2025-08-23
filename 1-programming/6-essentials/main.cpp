// main.cpp
// C++ examples demonstrating programming essentials like comments, input/output, and error handling.

#include <iostream>
#include <string>

void greet(const std::string& name) {
    // Function to greet user by name
    std::cout << "Hello, " << name << std::endl;
}

int main() {
    std::string name;
    std::cout << "Enter your name: ";
    std::getline(std::cin, name);

    if (name.empty()) {
        std::cerr << "Error: Name cannot be empty!" << std::endl;
        return 1; // Exit with error code
    }

    greet(name);
    return 0;
}
