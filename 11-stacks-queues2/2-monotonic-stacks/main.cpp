// Monotonic Stack - C++ Example

#include <iostream>
#include <vector>
#include <stack>

std::vector<int> nextGreaterElements(const std::vector<int>& arr) {
    std::vector<int> result(arr.size(), -1);
    std::stack<int> s;

    for (int i = 0; i < arr.size(); ++i) {
        while (!s.empty() && arr[s.top()] < arr[i]) {
            int idx = s.top(); s.pop();
            result[idx] = arr[i];
        }
        s.push(i);
    }

    return result;
}

int main() {
    std::vector<int> arr = {2,1,2,4,3};
    std::vector<int> result = nextGreaterElements(arr);

    std::cout << "Next greater elements: ";
    for (int val : result) std::cout << val << " ";
    std::cout << std::endl;
    return 0;
}
