// main.cpp
// C++ examples demonstrating control flow statements.

#include <iostream>

void checkNumber(int num) {
    if (num > 0) {
        std::cout << num << " is Positive" << std::endl;
    } else if (num == 0) {
        std::cout << num << " is Zero" << std::endl;
    } else {
        std::cout << num << " is Negative" << std::endl;
    }
}

int main() {
    for (int i = -1; i <= 1; i++) {
        checkNumber(i);
    }
    return 0;
}
