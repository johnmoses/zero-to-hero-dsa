// Application Examples - C++

#include <iostream>
#include <vector>

int countInRange(const std::vector<int>& prefix, int left, int right) {
    if (left == 0) return prefix[right];
    return prefix[right] - prefix[left - 1];
}

int main() {
    std::vector<int> arr = {1, 2, 2, 3, 3, 3, 4};
    int maxVal = *max_element(arr.begin(), arr.end());
    std::vector<int> freq(maxVal + 1, 0);

    for (int num : arr) freq[num]++;

    std::vector<int> prefixFreq(freq.size(), 0);
    prefixFreq[0] = freq;
    for (size_t i = 1; i < freq.size(); i++) {
        prefixFreq[i] = prefixFreq[i - 1] + freq[i];
    }

    std::cout << "Count of numbers between 2 and 3: " << countInRange(prefixFreq, 2, 3) << std::endl;
    return 0;
}
