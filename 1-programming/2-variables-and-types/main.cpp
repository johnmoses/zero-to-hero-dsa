// main.cpp
// C++ examples for variables and data types.

#include <iostream>
#include <string>

int main() {
    int age = 25;
    double height = 5.9;
    bool isStudent = true;
    char grade = 'A';
    std::string name = "Alice";

    std::cout << "Age: " << age << std::endl;
    std::cout << "Height: " << height << std::endl;
    std::cout << "Is Student: " << (isStudent ? "true" : "false") << std::endl;
    std::cout << "Grade: " << grade << std::endl;
    std::cout << "Name: " << name << std::endl;

    return 0;
}
