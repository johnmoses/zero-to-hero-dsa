// Tabulation - C++ example

#include <iostream>
#include <vector>

int fib(int n) {
    if (n <= 1) return n;
    std::vector<int> dp(n+1, 0);
    dp[1] = 1;

    for (int i = 2; i <= n; ++i)
        dp[i] = dp[i-1] + dp[i-2];

    return dp[n];
}

int main() {
    std::cout << fib(10) << std::endl;  // Output: 55
    return 0;
}
