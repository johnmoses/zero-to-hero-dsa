/*
A Simple Algorithm:
    
Fibonacci numbers using native approach

Fibonacci numbers is a sequence such that
each number is the sum of the two preceeding ones starting from 0 and 1
So we have 0, 1, 1, 2, 3, 5, 8, 13, 21
*/

#include <iostream>
using namespace std;

int main()
{
    int n;
    cout << "Enter the number of terms: ";
    cin >> n;

    int a = 0, b = 1, c;

    cout << "Fibonacci Series: ";

    for (int i = 0; i < n; i++)
    {
        cout << a << " ";
        c = a + b;
        a = b;
        b = c;
    }

    return 0;
}