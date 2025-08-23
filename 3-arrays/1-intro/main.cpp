// Arrays - C++ Example

#include <iostream>

int main() {
    int arr[] = {1, 2, 3, 4, 5};

    std::cout << "Element at index 2: " << arr[2] << std::endl;  // Output: 3

    arr = 10;
    std::cout << "Modified array: ";
    for (int i = 0; i < 5; i++) {
        std::cout << arr[i] << ' ';
    }
    std::cout << std::endl;

    return 0;
}
