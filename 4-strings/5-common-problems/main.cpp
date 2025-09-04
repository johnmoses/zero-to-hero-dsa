// Common problems with strings in C++
#include <iostream>
#include <string>

int main() {
    // Problem 1: Uninitialized string
    std::string uninitialized; // Default constructor initializes to empty string
    std::cout << "Uninitialized string (should be empty): '" << uninitialized << "'" << std::endl;  // Output: Uninitialized string (should be empty): ''  
    return 0;
}