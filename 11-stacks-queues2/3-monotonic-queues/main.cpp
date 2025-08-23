// Monotonic Queue - C++ Example

#include <iostream>
#include <vector>
#include <deque>

std::vector<int> maxSlidingWindow(const std::vector<int>& nums, int k) {
    std::deque<int> dq;
    std::vector<int> result;

    for (int i = 0; i < nums.size(); i++) {
        while (!dq.empty() && nums[dq.back()] < nums[i])
            dq.pop_back();
        dq.push_back(i);

        if (dq.front() == i - k)
            dq.pop_front();

        if (i >= k - 1)
            result.push_back(nums[dq.front()]);
    }
    return result;
}

int main() {
    std::vector<int> nums = {1,3,-1,-3,5,3,6,7};
    int k = 3;

    std::vector<int> max_vals = maxSlidingWindow(nums, k);
    std::cout << "Sliding window maximum: ";
    for (int val : max_vals) std::cout << val << " ";
    std::cout << std::endl;

    return 0;
}
