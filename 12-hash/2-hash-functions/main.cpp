// Hash Function - C++ Example

#include <iostream>
#include <vector>

int simpleHash(int key, int size) {
    return key % size;
}

int main() {
    int size = 10;
    std::vector<int> keys = {15, 25, 35};
    for (int key : keys) {
        std::cout << "Hashed key for " << key << ": " << simpleHash(key, size) << std::endl;
    }
    return 0;
}
