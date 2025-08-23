// String Searching - C++ Example

#include <iostream>
#include <string>

int main() {
    std::string text = "Hello, world!";
    std::string substring = "world";

    size_t index = text.find(substring);
    if (index != std::string::npos) {
        std::cout << "Index of 'world': " << index << std::endl;
    } else {
        std::cout << "'world' not found" << std::endl;
    }
    return 0;
}
