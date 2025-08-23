// Monotonic Stack - C++ example (Next Greater Element)

#include <iostream>
#include <vector>
#include <stack>

using namespace std;

vector<int> nextGreaterElements(const vector<int>& nums) {
    vector<int> result(nums.size(), -1);
    stack<int> s;

    for (int i = 0; i < nums.size(); ++i) {
        while (!s.empty() && nums[s.top()] < nums[i]) {
            result[s.top()] = nums[i];
            s.pop();
        }
        s.push(i);
    }
    return result;
}

int main() {
    vector<int> nums = {2, 1, 2, 4, 3};
    vector<int> res = nextGreaterElements(nums);
    for (int val : res)
        cout << val << " ";
    cout << endl;  // Output: 4 2 4 -1 -1
    return 0;
}
