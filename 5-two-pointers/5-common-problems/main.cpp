// Common Two Pointers Problems - C++ Example

#include <iostream>
#include <vector>
#include <algorithm>

int maxArea(const std::vector<int>& height) {
    int left = 0, right = height.size() - 1;
    int max_area = 0;
    while (left < right) {
        int width = right - left;
        int curr_area = std::min(height[left], height[right]) * width;
        max_area = std::max(max_area, curr_area);
        if (height[left] < height[right]) left++;
        else right--;
    }
    return max_area;
}

int main() {
    std::vector<int> heights = {1,8,6,2,5,4,8,3,7};
    std::cout << "Max water container area: " << maxArea(heights) << std::endl;
    return 0;
}
