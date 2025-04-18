/*
Recursion

Write a simple recursion algorithm
to print numbers from 1 to n in normal order and then print numbers from n to 1 in reverse order.
*/
#include <iostream>
using namespace std;

void print(int n)
{
    if (n == 0)
        return;
    cout << n << " ";
    print(n - 1);
    cout << n << " ";
}

int main()
{
    int n;
    cin >> n;
    print(n);
    return 0;
}