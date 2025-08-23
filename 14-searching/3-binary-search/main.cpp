// Binary Search - C++ Example

#include <iostream>
#include <vector>

int binarySearch(const std::vector<int>& arr, int target) {
    int low = 0, high = arr.size()-1;
    while(low <= high) {
        int mid = low + (high-low)/2;
        if (arr[mid] == target) {
            return mid;
        }
        else if(arr[mid] < target) {
            low = mid+1;
        }
        else {
            high = mid-1;
        }
    }
    return -1;
}

int main() {
    std::vector<int> arr = {1,2,3,4,5,6,7};
    std::cout << "Index of 4: " << binarySearch(arr, 4) << std::endl;
    return 0;
}
