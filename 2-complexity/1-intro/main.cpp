// Introduction to Complexity - C++ Example

#include <iostream>
#include <vector>

int linear_search(const std::vector<int>& arr, int target) {
    for (size_t i = 0; i < arr.size(); i++) {
        if (arr[i] == target)
            return i; // return index
    }
    return -1; // not found
}

int main() {
    std::vector<int> data = {4, 7, 1, 3, 9};
    std::cout << "Index of 3: " << linear_search(data, 3) << std::endl;
    return 0;
}
