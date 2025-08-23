// Merge Sort - C++ Example

#include <iostream>
#include <vector>

std::vector<int> merge(const std::vector<int>& left, const std::vector<int>& right) {
    std::vector<int> result;
    int i = 0, j = 0;
    while(i < left.size() && j < right.size()) {
        if(left[i] < right[j]) {
            result.push_back(left[i++]);
        } else {
            result.push_back(right[j++]);
        }
    }
    while(i < left.size()) result.push_back(left[i++]);
    while(j < right.size()) result.push_back(right[j++]);
    return result;
}

std::vector<int> mergeSort(const std::vector<int>& arr) {
    if(arr.size() <=1) return arr;
    int mid = arr.size()/2;
    std::vector<int> left(arr.begin(), arr.begin()+mid);
    std::vector<int> right(arr.begin()+mid, arr.end());
    left = mergeSort(left);
    right = mergeSort(right);
    return merge(left, right);
}

int main() {
    std::vector<int> arr = {38,27,43,3,9,82,10};
    std::vector<int> sorted_arr = mergeSort(arr);

    std::cout << "Sorted array: ";
    for(int x: sorted_arr) std::cout << x << " ";
    std::cout << std::endl;
    return 0;
}
