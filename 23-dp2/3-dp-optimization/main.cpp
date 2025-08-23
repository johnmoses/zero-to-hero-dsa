// DP Optimization - C++ example (Space Optimized Fibonacci)

#include <iostream>

int fib(int n) {
    if (n <= 1) return n;
    int prev = 0, curr = 1;
    for (int i = 2; i <= n; ++i) {
        int next = prev + curr;
        prev = curr;
        curr = next;
    }
    return curr;
}

int main() {
    std::cout << fib(10) << std::endl;  // Output: 55
    return 0;
}
