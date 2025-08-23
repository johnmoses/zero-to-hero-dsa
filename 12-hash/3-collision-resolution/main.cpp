// Collision Resolution - C++ Example (Chaining)

#include <iostream>
#include <vector>
#include <list>
#include <string>

class HashMap {
    std::vector<std::list<std::pair<std::string, int>>> buckets;
    int size;

    int hash(const std::string& key) {
        std::hash<std::string> hasher;
        return hasher(key) % size;
    }

public:
    HashMap(int sz = 10) : size(sz), buckets(sz) {}

    void insert(const std::string& key, int value) {
        int idx = hash(key);
        for (auto& kv : buckets[idx]) {
            if (kv.first == key) {
                kv.second = value;
                return;
            }
        }
        buckets[idx].emplace_back(key, value);
    }

    int get(const std::string& key) {
        int idx = hash(key);
        for (auto& kv : buckets[idx]) {
            if (kv.first == key) return kv.second;
        }
        return -1;  // Not found
    }
};

int main() {
    HashMap hmap;
    hmap.insert("apple", 3);
    hmap.insert("banana", 5);
    std::cout << "Apple count: " << hmap.get("apple") << std::endl;
    return 0;
}
