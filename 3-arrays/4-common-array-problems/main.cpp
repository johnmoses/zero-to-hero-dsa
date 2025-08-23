// Common Array Problems - C++ Example

#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> arr = {1, 3, 2, 8, 5};

    // Find maximum
    int max_val = *std::max_element(arr.begin(), arr.end());
    std::cout << "Maximum value: " << max_val << std::endl;

    // Reverse array
    std::reverse(arr.begin(), arr.end());
    std::cout << "Reversed array: ";
    for (int val : arr) std::cout << val << " ";
    std::cout << std::endl;

    // Sum of subarray [1, 4)
    int sub_sum = 0;
    for (int i = 1; i < 4; i++) {
        sub_sum += arr[i];
    }
    std::cout << "Subarray sum: " << sub_sum << std::endl;

    return 0;
}
