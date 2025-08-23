// Cumulative Sums - C++ Example

#include <iostream>
#include <vector>

std::vector<int> cumulativeCountPositive(const std::vector<int>& arr) {
    std::vector<int> cumCount(arr.size());
    cumCount[0] = arr > 0 ? 1 : 0;
    for (size_t i = 1; i < arr.size(); i++) {
        cumCount[i] = cumCount[i - 1] + (arr[i] > 0 ? 1 : 0);
    }
    return cumCount;
}

int main() {
    std::vector<int> arr = {-1, 4, 2, -3, 5};
    std::vector<int> countPos = cumulativeCountPositive(arr);

    std::cout << "Cumulative count of positives: ";
    for (int val : countPos) std::cout << val << " ";
    std::cout << std::endl;
    return 0;
}
