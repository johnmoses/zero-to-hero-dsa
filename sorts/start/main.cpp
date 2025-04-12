/*
Simple Sort Algorithm

Write a basic sort algorithm that takes a list of numbers and returns a sorted list.

Example 1:
    Input: [1, 5, 2, 3, 4]
    Output: [1, 2, 3, 4, 5]

Example 2:
    Input: [5, 4, 3, 2, 1]
    Output: [1, 2, 3, 4, 5]
*/

#include <iostream>
using namespace std;

int main() {
    int arr[] = {5, 4, 3, 2, 1};
    int n = sizeof(arr) / sizeof(arr[0]);

    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }

    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }

    return 0;
}