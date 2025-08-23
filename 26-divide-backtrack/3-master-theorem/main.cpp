// Merge Sort illustrating recurrence solved by Master Theorem

#include <iostream>
#include <vector>

using namespace std;

void merge(vector<int>& arr, int left, int mid, int right) {
    vector<int> temp(right - left + 1);
    int i = left, j = mid + 1, k = 0;

    while(i <= mid && j <= right) {
        if(arr[i] < arr[j]) temp[k++] = arr[i++];
        else temp[k++] = arr[j++];
    }
    while(i <= mid) temp[k++] = arr[i++];
    while(j <= right) temp[k++] = arr[j++];

    for(int idx = 0; idx < k; ++idx) arr[left + idx] = temp[idx];
}

void mergeSort(vector<int>& arr, int left, int right) {
    if(left >= right) return;
    int mid = left + (right - left) / 2;
    mergeSort(arr, left, mid);
    mergeSort(arr, mid+1, right);
    merge(arr, left, mid, right);
}

int main() {
    vector<int> arr = {5, 2, 4, 6, 1, 3};
    mergeSort(arr, 0, (int)arr.size() - 1);
    cout << "Sorted array: ";
    for(int num : arr) cout << num << " ";
    cout << endl;
    return 0;
}
