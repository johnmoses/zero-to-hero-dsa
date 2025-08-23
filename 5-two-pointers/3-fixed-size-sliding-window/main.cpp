// Fixed Size Sliding Window - C++ Example

#include <iostream>
#include <vector>
#include <algorithm>

int maxSumSubarray(const std::vector<int>& arr, int k) {
    int windowSum = 0;
    for (int i = 0; i < k; i++)
        windowSum += arr[i];
    int maxSum = windowSum;
    
    for (int i = k; i < arr.size(); i++) {
        windowSum += arr[i] - arr[i - k];
        maxSum = std::max(maxSum, windowSum);
    }
    return maxSum;
}

int main() {
    std::vector<int> arr = {2,1,5,1,3,2};
    int k = 3;
    std::cout << "Maximum sum of subarray of size " << k << ": " << maxSumSubarray(arr, k) << std::endl;
    return 0;
}
