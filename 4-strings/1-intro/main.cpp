// Strings - C++ Example

#include <iostream>
#include <string>

int main() {
    std::string text = "Hello, World!";
    std::cout << "Original string: " << text << std::endl;

    // Concatenation
    std::string greeting = text + " Welcome!";
    std::cout << "Concatenated string: " << greeting << std::endl;

    // Substring
    std::cout << "Substring (7,5): " << text.substr(7, 5) << std::endl;

    return 0;
}
