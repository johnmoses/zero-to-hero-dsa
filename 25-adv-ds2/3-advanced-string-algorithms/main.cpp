// Advanced String Algorithms - C++ example (KMP pattern search)

#include <iostream>
#include <vector>
#include <string>

std::vector<int> computeLPS(const std::string& pattern) {
    std::vector<int> lps(pattern.size(), 0);
    int length = 0;
    int i = 1;
    while(i < pattern.size()) {
        if(pattern[i] == pattern[length]) {
            length++;
            lps[i] = length;
            i++;
        } else {
            if(length != 0)
                length = lps[length - 1];
            else {
                lps[i] = 0;
                i++;
            }
        }
    }
    return lps;
}

std::vector<int> kmpSearch(const std::string& text, const std::string& pattern) {
    std::vector<int> lps = computeLPS(pattern);
    std::vector<int> positions;
    int i = 0, j = 0;

    while(i < text.size()) {
        if(text[i] == pattern[j]) {
            i++; j++;
            if(j == pattern.size()) {
                positions.push_back(i - j);
                j = lps[j-1];
            }
        } else {
            if(j != 0)
                j = lps[j-1];
            else
                i++;
        }
    }
    return positions;
}

int main() {
    std::string text = "ababcabcabababd";
    std::string pattern = "ababd";

    std::vector<int> positions = kmpSearch(text, pattern);
    for(int pos : positions)
        std::cout << pos << " ";
    std::cout << std::endl;
    return 0;
}
