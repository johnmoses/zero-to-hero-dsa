// Two Pointers Technique - C++ Example

#include <iostream>
#include <vector>

int removeDuplicates(std::vector<int>& arr) {
    if (arr.empty()) return 0;
    int writeIndex = 1;
    for (int readIndex = 1; readIndex < arr.size(); ++readIndex) {
        if (arr[readIndex] != arr[readIndex-1]) {
            arr[writeIndex] = arr[readIndex];
            writeIndex++;
        }
    }
    return writeIndex;
}

int main() {
    std::vector<int> arr = {1,1,2,2,3,4,4};
    int newLength = removeDuplicates(arr);

    std::cout << "Array without duplicates: ";
    for (int i = 0; i < newLength; ++i)
        std::cout << arr[i] << ' ';
    std::cout << std::endl;

    return 0;
}
