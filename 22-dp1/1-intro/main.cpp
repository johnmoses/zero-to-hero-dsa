// Dynamic Programming Intro - C++ example
// Compute Fibonacci numbers using memoization

#include <iostream>
#include <unordered_map>

int fib(int n, std::unordered_map<int,int>& memo) {
    if (memo.find(n) != memo.end()) return memo[n];
    if (n <= 1) return n;
    memo[n] = fib(n-1, memo) + fib(n-2, memo);
    return memo[n];
}

int main() {
    int n = 10;
    std::unordered_map<int,int> memo;
    std::cout << "Fibonacci number at position " << n << " is " << fib(n, memo) << std::endl;
    return 0;
}
