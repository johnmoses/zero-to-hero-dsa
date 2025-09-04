// Search Problem Examples - C++ Example

#include <iostream>
#include <vector>

int countOnes(const std::vector<int>& arr) {
    int low = 0, high = arr.size()-1;
    int count = 0;
    while (low <= high) {
        int mid = low + (high - low)/2;
        if (arr[mid] == 1) {
            count = arr.size() - mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    return count;
}

int main() {
    std::vector<int> arr = {0,0,0,1,1,1,1};
    std::cout << "Count of ones: " << countOnes(arr) << std::endl;
    return 0;
}
