/*
Arrays

Write code to show the basic functionality or behavior of an array
this includes selecting, slicing, adding, removing, sorting, searching, iterating etc.
*/

#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int n = sizeof(arr) / sizeof(arr[0]);
    cout << "Array: ";
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
    cout << "Selecting: " << arr[0] << endl;
    cout << "Slicing: ";
    for (int i = 0; i < 5; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
    cout << "Adding: ";
    arr[n] = 11;
    for (int i = 0; i < n + 1; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
    cout << "Removing: ";
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
    cout << "Sorting: ";
    sort(arr, arr + n);
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
    cout << "Searching: ";
    int key = 5;
    int index = -1;
    for (int i = 0; i < n; i++)
    {
        if (arr[i] == key)
        {
            index = i;
            break;
        }
    }
    if (index == -1)
    {
        cout << "Not found" << endl;
    }
    else
    {
        cout << "Found at index " << index << endl;
    }
    cout << "Iterating: ";
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
    return 0;
}