// Two Pointers - C++ Example

#include <iostream>
#include <vector>
#include <utility>

std::pair<int,int> twoSumSorted(const std::vector<int>& arr, int target) {
    int left = 0, right = arr.size() - 1;
    while (left < right) {
        int current_sum = arr[left] + arr[right];
        if (current_sum == target) {
            return {left, right};
        } else if (current_sum < target) {
            left++;
        } else {
            right--;
        }
    }
    return {-1, -1};
}

int main() {
    std::vector<int> arr = {1, 2, 3, 4, 6};
    int target = 6;
    auto result = twoSumSorted(arr, target);
    std::cout << "Indices: " << result.first << ", " << result.second << std::endl;
    return 0;
}
