// String Basics - C++ Example

#include <iostream>
#include <string>

int main() {
    std::string text = "hello";

    std::cout << "Length: " << text.length() << std::endl;
    std::cout << "First character: " << text[0] << std::endl;
    std::string upper_text;
    for (char c : text) upper_text += toupper(c);
    std::cout << "Uppercase: " << upper_text << std::endl;
    std::cout << "Contains 'll': " << (text.find("ll") != std::string::npos ? "true" : "false") << std::endl;

    return 0;
}
