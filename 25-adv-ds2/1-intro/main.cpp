// Advanced Data Structures 2 - Intro C++ example
// Bit manipulation: Counting set bits

#include <iostream>

int countSetBits(int n) {
    int count = 0;
    while (n) {
        n &= (n - 1);
        count++;
    }
    return count;
}

int main() {
    int num = 29; // Binary: 11101
    std::cout << countSetBits(num) << std::endl;  // Output: 4
    return 0;
}
