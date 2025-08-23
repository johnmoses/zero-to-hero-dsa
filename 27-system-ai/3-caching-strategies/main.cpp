// Caching Strategies - C++ example (LRU Cache)

#include <iostream>
#include <unordered_map>
#include <list>

using namespace std;

class LRUCache {
    int capacity;
    list<pair<int, int>> cacheList;
    unordered_map<int, list<pair<int, int>>::iterator> cacheMap;

public:
    LRUCache(int cap) : capacity(cap) {}

    int get(int key) {
        if (cacheMap.find(key) == cacheMap.end()) return -1;
        cacheList.splice(cacheList.begin(), cacheList, cacheMap[key]);
        return cacheMap[key]->second;
    }

    void put(int key, int value) {
        if (cacheMap.find(key) != cacheMap.end()) {
            cacheList.splice(cacheList.begin(), cacheList, cacheMap[key]);
            cacheMap[key]->second = value;
            return;
        }
        if ((int)cacheList.size() == capacity) {
            int delKey = cacheList.back().first;
            cacheList.pop_back();
            cacheMap.erase(delKey);
        }
        cacheList.emplace_front(key, value);
        cacheMap[key] = cacheList.begin();
    }
};

int main() {
    LRUCache lru(2);
    lru.put(1, 1);
    lru.put(2, 2);
    cout << lru.get(1) << endl; // Output: 1
    lru.put(3, 3);
    cout << lru.get(2) << endl; // Output: -1 (evicted)
    return 0;
}

