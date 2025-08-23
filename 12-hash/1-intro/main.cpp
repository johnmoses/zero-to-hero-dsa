// Hashing - C++ Example

#include <iostream>
#include <unordered_map>

int main() {
    std::unordered_map<std::string, int> hash_map;

    // Insert
    hash_map["apple"] = 3;
    hash_map["banana"] = 5;

    // Lookup
    std::cout << "Apple count: " << hash_map["apple"] << std::endl;

    // Update
    hash_map["apple"] += 2;
    std::cout << "Updated apple count: " << hash_map["apple"] << std::endl;

    return 0;
}
