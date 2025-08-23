// Classic Divide and Conquer - C++ example

#include <iostream>
#include <vector>

using namespace std;

int binarySearch(const vector<int>& arr, int target) {
    int left = 0, right = (int)arr.size() - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == target) return mid;
        else if (arr[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}

int main() {
    vector<int> arr = {1,3,5,7,9,11,13};
    int target = 7;
    cout << "Index of " << target << ": " << binarySearch(arr, target) << endl;
    return 0;
}
