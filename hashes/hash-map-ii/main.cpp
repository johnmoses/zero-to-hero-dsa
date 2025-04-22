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

    return 0;
}
