/*
Selection sort

Given an array, [5, 3, 6, 2, 10], write a selection sort algorithm to sort the array in ascending order.
The output should be [2, 3, 5, 6, 10]
*/
#include <iostream>
using namespace std;

int main()
{
    int arr[5] = {5, 3, 6, 2, 10};
    int n = 5;
    for (int i = 0; i < n - 1; i++)
    {
        int min = i;
        for (int j = i + 1; j < n; j++)
        {
            if (arr[j] < arr[min])
            {
                min = j;
            }
        }
        int temp = arr[min];
        arr[min] = arr[i];
        arr[i] = temp;
    }
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    return 0;
}
