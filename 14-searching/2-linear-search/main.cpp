// Linear Search - C++ Example

#include <iostream>
#include <vector>

int linearSearch(const std::vector<int>& arr, int target) {
    for (int i=0; i < arr.size(); i++) {
        if(arr[i] == target) return i;
    }
    return -1;
}

int main() {
    std::vector<int> arr = {5,3,1,9,7};
    std::cout << "Index of 9: " << linearSearch(arr, 9) << std::endl;
    return 0;
}
