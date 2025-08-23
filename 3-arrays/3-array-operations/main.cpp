// Array Operations - C++ Example

#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> arr = {1, 2, 3, 4, 5};

    // Traversal
    for (int element : arr) {
        std::cout << "Element: " << element << std::endl;
    }

    // Insertion (append)
    arr.push_back(6);

    // Deletion (remove by value)
    arr.erase(std::remove(arr.begin(), arr.end(), 2), arr.end());

    // Searching (find)
    auto it = std::find(arr.begin(), arr.end(), 4);
    int index = (it != arr.end()) ? std::distance(arr.begin(), it) : -1;
    std::cout << "Index of 4: " << index << std::endl;

    // Updating
    arr[0] = 10;

    // Print updated array
    std::cout << "Updated array: ";
    for (int e : arr) std::cout << e << " ";
    std::cout << std::endl;

    return 0;
}
