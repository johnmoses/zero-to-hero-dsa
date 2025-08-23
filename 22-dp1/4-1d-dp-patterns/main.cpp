// 1D DP Patterns - C++ example (Climbing Stairs)

#include <iostream>
#include <vector>

int climbStairs(int n) {
    if (n <= 2) return n;
    std::vector<int> dp(n+1);
    dp[1] = 1;
    dp = 2;

    for (int i = 3; i <= n; ++i)
        dp[i] = dp[i-1] + dp[i-2];

    return dp[n];
}

int main() {
    std::cout << climbStairs(10) << std::endl;  // Output: 89
    return 0;
}
