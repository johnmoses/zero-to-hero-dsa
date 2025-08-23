// Difference Arrays - C++ Example

#include <iostream>
#include <vector>

void updateRange(std::vector<int>& diff, int l, int r, int val) {
    diff[l] += val;
    if (r + 1 < diff.size()) {
        diff[r + 1] -= val;
    }
}

std::vector<int> reconstructArray(const std::vector<int>& diff) {
    std::vector<int> res(diff.size() - 1);
    int curr = 0;
    for (size_t i = 0; i < res.size(); i++) {
        curr += diff[i];
        res[i] = curr;
    }
    return res;
}

int main() {
    std::vector<int> arr = {1, 2, 3, 4, 5};
    std::vector<int> diff(arr.size() + 1, 0);
    for (size_t i = 0; i < arr.size(); i++) {
        diff[i] += arr[i];
        diff[i + 1] -= arr[i];
    }

    updateRange(diff, 1, 3, 5);
    std::vector<int> result = reconstructArray(diff);

    std::cout << "Array after range update: ";
    for (int val : result) std::cout << val << " ";
    std::cout << std::endl;

    return 0;
}
