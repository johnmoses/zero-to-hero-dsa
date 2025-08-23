// Divide and Conquer & Backtracking - C++ example

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Merge function for merge sort
vector<int> merge(const vector<int>& left, const vector<int>& right) {
    vector<int> result;
    int i = 0, j = 0;
    while (i < (int)left.size() && j < (int)right.size()) {
        if (left[i] < right[j]) result.push_back(left[i++]);
        else result.push_back(right[j++]);
    }
    while (i < (int)left.size()) result.push_back(left[i++]);
    while (j < (int)right.size()) result.push_back(right[j++]);
    return result;
}

// Merge sort using divide and conquer
vector<int> mergeSort(const vector<int>& arr) {
    if (arr.size() <= 1) return arr;
    int mid = arr.size() / 2;
    vector<int> left(arr.begin(), arr.begin() + mid);
    vector<int> right(arr.begin() + mid, arr.end());
    return merge(mergeSort(left), mergeSort(right));
}

// Backtracking subset sum
bool subsetSum(const vector<int>& nums, int target, int index = 0) {
    if (target == 0) return true;
    if (target < 0 || index >= (int)nums.size()) return false;
    // Include nums[index]
    if (subsetSum(nums, target - nums[index], index + 1)) return true;
    // Exclude nums[index]
    return subsetSum(nums, target, index + 1);
}

int main() {
    vector<int> arr = {3, 6, 1, 7, 2, 5};
    vector<int> sortedArr = mergeSort(arr);
    cout << "Sorted array: ";
    for (int x : sortedArr) cout << x << ' ';
    cout << endl;

    vector<int> nums = {3, 34, 4, 12, 5, 2};
    int target = 9;
    cout << "Subset sum exists: " << boolalpha << subsetSum(nums, target) << endl;

    return 0;
}
