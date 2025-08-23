// Search in Rotated Sorted Array - C++ Example

#include <iostream>
#include <vector>

int searchRotated(const std::vector<int>& arr, int target) {
    int low = 0, high = arr.size()-1;
    while (low <= high) {
        int mid = low + (high - low)/2;
        if (arr[mid] == target) return mid;

        if (arr[low] <= arr[mid]) {
            if (arr[low] <= target && target < arr[mid]) high = mid-1;
            else low = mid+1;
        } else {
            if (arr[mid] < target && target <= arr[high]) low = mid+1;
            else high = mid-1;
        }
    }
    return -1;
}

int main() {
    std::vector<int> arr = {4,5,6,7,0,1,2};
    std::cout << "Index of 0: " << searchRotated(arr, 0) << std::endl;
    return 0;
}
