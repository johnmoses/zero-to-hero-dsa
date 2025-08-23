// Variable Size Sliding Window - C++ Example

#include <iostream>
#include <vector>
#include <climits>

int minSubarrayLen(int target, const std::vector<int>& arr) {
    int start = 0, currSum = 0, minLen = INT_MAX;

    for (int end = 0; end < arr.size(); ++end) {
        currSum += arr[end];
        while (currSum >= target) {
            minLen = std::min(minLen, end - start + 1);
            currSum -= arr[start++];
        }
    }

    return minLen == INT_MAX ? 0 : minLen;
}

int main() {
    std::vector<int> arr = {2,3,1,2,4,3};
    int target = 7;
    std::cout << "Minimum subarray length with sum >= " << target << ": " << minSubarrayLen(target, arr) << std::endl;
    return 0;
}
