// Sorting Introduction - C++ Example

#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> arr = {5, 3, 8, 4, 2};
    std::vector<int> sorted_arr = arr;
    std::sort(sorted_arr.begin(), sorted_arr.end());

    std::cout << "Original array: ";
    for (int x : arr) std::cout << x << " ";
    std::cout << "\nSorted array: ";
    for (int x : sorted_arr) std::cout << x << " ";
    std::cout << std::endl;
    return 0;
}
