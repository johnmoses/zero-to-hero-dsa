/*
Suppose you were given a list of strings [“hello”, everyone, “we”, “are”, “learning, “sorting”],
what is the most efficient way of sorting it?
*/
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    vector<string> v = {"hello", "everyone", "we", "are", "learning", "sorting"};
    sort(v.begin(), v.end());
    for (auto i : v)
    {
        cout << i << " ";
    }
    cout << endl;
    return 0;
}