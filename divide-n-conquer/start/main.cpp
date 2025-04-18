/*
Given a set of numbers, write a divide and conquer algorithm to sort the numbers.

Example 1:
    Input: [3, 7, 6, -10, 15, 23.5, 55, -13]
    Output: [-13, -10, 3, 6, 7, 15, 23.5, 55]
*/
#include <iostream>
#include <vector>
using namespace std;

void merge(vector<double>& arr, int start, int mid, int end) {
    int left = start;
    int right = mid + 1;
    vector<double> temp;

    while (left <= mid && right <= end) {
        if (arr[left] <= arr[right]) {
            temp.push_back(arr[left]);
            left++;
        } else {
            temp.push_back(arr[right]);
            right++;
        }
    }

    while (left <= mid) {
        temp.push_back(arr[left]);
        left++;
    }

    while (right <= end) {
        temp.push_back(arr[right]);
        right++;
    }

    for (int i = start; i <= end; i++) {
        arr[i] = temp[i - start];
    }
}

void mergeSort(vector<double>& arr, int start, int end) {
    if (start < end) {
        int mid = (start + end) / 2;
        mergeSort(arr, start, mid);
        mergeSort(arr, mid + 1, end);
        merge(arr, start, mid, end);
    }
}

int main() {
    vector<double> arr = {3, 7, 6, -10, 15, 23.5, 55, -13};
    mergeSort(arr, 0, arr.size() - 1);

    cout << "Sorted array: ";
    for (double num : arr) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
