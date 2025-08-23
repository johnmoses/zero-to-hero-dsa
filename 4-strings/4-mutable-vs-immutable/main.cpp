// Mutable vs Immutable Strings - C++ Example

#include <iostream>
#include <string>

int main() {
    std::string text = "hello";
    std::cout << "Original text: " << text << std::endl;

    text[0] = 'j';  // Mutable: changing first character
    std::cout << "Modified text: " << text << std::endl;

    return 0;
}
