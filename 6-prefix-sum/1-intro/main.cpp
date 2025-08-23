// Prefix Sum - C++ Example

#include <iostream>
#include <vector>

std::vector<int> prefixSum(const std::vector<int>& arr) {
    std::vector<int> prefix(arr.size());
    prefix[0] = arr;
    for (size_t i = 1; i < arr.size(); i++) {
        prefix[i] = prefix[i - 1] + arr[i];
    }
    return prefix;
}

int main() {
    std::vector<int> arr = {1, 2, 3, 4};
    std::vector<int> prefix = prefixSum(arr);

    std::cout << "Prefix sum array: ";
    for (int val : prefix) std::cout << val << " ";
    std::cout << std::endl;

    int result = prefix[3] - prefix;
    std::cout << "Sum from index 1 to 3: " << result << std::endl;
    return 0;
}
