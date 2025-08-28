// Big O Basics - C++ Example

#include <iostream>
#include <vector>

int constant_time(const std::vector<int>& items) {
    return items.empty() ? 0 : items[0];  // O(1)
}

int logarithmic_time(int n) {
    int count = 0;
    while (n > 1) {
        n /= 2;
        count++;
    }
    return count;  // O(log n)
}

int quadratic_time(const std::vector<int>& items) {
    int count = 0;
    for (size_t i = 0; i < items.size(); i++) {
        for (size_t j = 0; j < items.size(); j++) {
            count++;
        }
    }
    return count;  // O(n^2)
}

int main() {
    std::vector<int> data = {1, 2, 3};
    std::cout << "Constant time result: " << constant_time(data) << std::endl;
    std::cout << "Logarithmic steps: " << logarithmic_time(16) << std::endl;
    std::cout << "Quadratic operations: " << quadratic_time(data) << std::endl;
    return 0;
}
