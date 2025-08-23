// Searching Introduction - C++ Example

#include <iostream>
#include <vector>

int linearSearch(const std::vector<int>& arr, int target) {
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] == target) return i;
    }
    return -1;
}

int binarySearch(const std::vector<int>& arr, int target) {
    int low = 0, high = arr.size() -1;
    while (low <= high) {
        int mid = low + (high - low)/2;
        if (arr[mid] == target) return mid;
        else if (arr[mid] < target) low = mid +1;
        else high = mid -1;
    }
    return -1;
}

int main() {
    std::vector<int> arr = {2,4,6,8,10};
    std::cout << "Linear search index: " << linearSearch(arr,8) << std::endl;
    std::cout << "Binary search index: " << binarySearch(arr,8) << std::endl;
    return 0;
}
