/* 
Hashes

Design a hash map with ability to insert, access and delete items.

Example 1:
    Input
    ["HashMap", "insert", "insert", "get", "get", "insert", "get", "delete", "get"]
    [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
    Output
    [null, null, null, 1, -1, null, 1, null, -1]

Constraints:
0 <= key, value <= 106
At most 104 calls will be made to put, get, and remove.
*/
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class HashMap {
private:
    unordered_map<int, int> map;
public:
    HashMap() {
        // Initialize your data structure here. 
    }
    
    void put(int key, int value) {
        map[key] = value;
    }
    
    int get(int key) {
        if (map.find(key) != map.end()) {
            return map[key];
        }
        return -1;
    }
    
    void remove(int key) {
        if (map.find(key) != map.end()) {
            map.erase(key);
        }
    }

    void print() {
        for (auto& pair : map) {
            cout << pair.first << ": " << pair.second << endl;
        }
    }
};

/*
Design a hash set with insert, contains and delete behaviours.

Example 1:
    ["HashSet", "insert", "insert", "contains", "contains", "insert", "contains", "delete", "contains"]
    [[], [1], [2], [1], [3], [2], [2], [2], [2]]
    Output
    [null, null, null, true, false, nul

Constraints:
0 <= key <= 106
At most 104 calls will be made to insert, delete, and contains.
*/
#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;
class HashSet {
private:
    unordered_set<int> set;
public:
    HashSet() {
        // Initialize your data structure here.
    }

    void add(int key) {
        set.insert(key);
    }

    bool contains(int key) {
        return set.find(key) != set.end();
    }

    void remove(int key) {
        if (set.find(key) != set.end()) {
            set.erase(key);
        }
    }

    void print() {
        for (auto& key : set) {
            cout << key << endl;
        }
    }
};

int main() {
    // Example usage
    HashMap hashMap;
    hashMap.put(1, 1);
    hashMap.put(2, 2);
    cout << hashMap.get(1) << endl; // Output: 1
    cout << hashMap.get(3) << endl; // Output: -1
    hashMap.put(2, 1);
    cout << hashMap.get(2) << endl; // Output: 1
    hashMap.remove(2);
    cout << hashMap.get(2) << endl; // Output: -1
    hashMap.print();

    HashSet hashSet;
    hashSet.add(1);
    hashSet.add(2);
    cout << boolalpha << hashSet.contains(1) << endl; // Output: true
    cout << boolalpha << hashSet.contains(3) << endl; // Output: false
    hashSet.add(2);
    cout << boolalpha << hashSet.contains(2) << endl; // Output: true
    hashSet.remove(2);
    cout << boolalpha << hashSet.contains(2) << endl; // Output: false
    hashSet.print();

    return 0;
}
