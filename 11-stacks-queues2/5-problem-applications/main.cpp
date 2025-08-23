// Problem Applications - C++ Example

#include <iostream>
#include <vector>
#include <stack>

int largestRectangleArea(const std::vector<int>& heights) {
    std::stack<int> stack;
    int maxArea = 0;
    std::vector<int> extendedHeights = heights;
    extendedHeights.push_back(0);

    for (int i = 0; i < extendedHeights.size(); ++i) {
        while (!stack.empty() && extendedHeights[stack.top()] > extendedHeights[i]) {
            int height = extendedHeights[stack.top()];
            stack.pop();
            int width = stack.empty() ? i : i - stack.top() -1;
            maxArea = std::max(maxArea, height * width);
        }
        stack.push(i);
    }
    return maxArea;
}

int main() {
    std::vector<int> heights = {2,1,5,6,2,3};
    std::cout << "Largest rectangle area: " << largestRectangleArea(heights) << std::endl;
    return 0;
}
