// Time and Space Complexity - C++ Example

#include <vector>

int sum_list(const std::vector<int>& items) {
    int total = 0;  // O(1) space
    for (int item : items) {  // O(n) time
        total += item;
    }
    return total;
}

std::vector<int> copy_list(const std::vector<int>& items) {
    std::vector<int> new_list;  // O(n) space
    for (int item : items) {     // O(n) time
        new_list.push_back(item);
    }
    return new_list;
}
