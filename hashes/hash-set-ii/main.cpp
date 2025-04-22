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
