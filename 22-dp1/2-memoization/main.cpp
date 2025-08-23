// Memoization - C++ example

#include <iostream>
#include <unordered_map>

int fib(int n, std::unordered_map<int,int>& memo) {
    if (memo.find(n) != memo.end()) return memo[n];
    if (n <= 1) return n;
    memo[n] = fib(n-1, memo) + fib(n-2, memo);
    return memo[n];
}

int main() {
    std::unordered_map<int,int> memo;
    std::cout << fib(10, memo) << std::endl;  // Output: 55
    return 0;
}
