// Best, Worst, and Average Case - C++ Example

#include <iostream>
#include <vector>

int linear_search(const std::vector<int>& arr, int target) {
    for (size_t i = 0; i < arr.size(); i++) {
        if (arr[i] == target)
            return i;
    }
    return -1;
}

int main() {
    std::vector<int> data = {1, 2, 3, 4, 5};

    std::cout << "Best case (target=1): " << linear_search(data, 1) << std::endl;
    std::cout << "Worst case (target=6): " << linear_search(data, 6) << std::endl;
    std::cout << "Average case (target=3): " << linear_search(data, 3) << std::endl;

    return 0;
}
