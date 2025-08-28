// Array Types - C++ Example

#include <iostream>

int main() {
    int arr_1d[] = {1, 2, 3};
    int arr_2d[2][2] = {{1, 2}, {3, 4}};

    std::cout << "1D array: ";
    for (int i = 0; i < 3; i++) {
        std::cout << arr_1d[i] << " ";
    }
    std::cout << std::endl;

    std::cout << "2D array:" << std::endl;
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            std::cout << arr_2d[i][j] << " ";
        }
        std::cout << std::endl;
    }
    return 0;
}
