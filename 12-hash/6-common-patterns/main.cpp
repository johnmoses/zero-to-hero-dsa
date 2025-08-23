// Common Hashing Problems - C++ Example

#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>

// Anagram check
bool areAnagrams(const std::string& s1, const std::string& s2) {
    if (s1.size() != s2.size()) return false;
    std::unordered_map<char, int> freq;
    for (char c : s1) freq[c]++;
    for (char c : s2) {
        if (--freq[c] < 0) return false;
    }
    return true;
}

// Intersection of arrays
std::vector<int> arrayIntersection(const std::vector<int>& arr1, const std::vector<int>& arr2) {
    std::unordered_set<int> set1(arr1.begin(), arr1.end());
    std::vector<int> result;
    for (int x : arr2) {
        if (set1.find(x) != set1.end()) {
            result.push_back(x);
        }
    }
    return result;
}

// Two sum
std::pair<int, int> twoSum(const std::vector<int>& nums, int target) {
    std::unordered_map<int, int> hash_map;
    for (int i = 0; i < nums.size(); i++) {
        int complement = target - nums[i];
        if (hash_map.find(complement) != hash_map.end()) {
            return {hash_map[complement], i};
        }
        hash_map[nums[i]] = i;
    }
    return {-1, -1};
}

int main() {
    std::cout << "Are 'listen' and 'silent' anagrams? " << (areAnagrams("listen", "silent") ? "Yes" : "No") << std::endl;

    std::vector<int> intersection = arrayIntersection({1,2,2,1}, {2,2});
    std::cout << "Intersection: ";
    for (int x : intersection) std::cout << x << " ";
    std::cout << std::endl;

    auto indices = twoSum({2,7,11,15}, 9);
    std::cout << "Two sum indices: (" << indices.first << ", " << indices.second << ")" << std::endl;

    return 0;
}
