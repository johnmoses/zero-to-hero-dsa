// Introduction to Trie and N-ary Tree Nodes - C++ Example

#include <iostream>
#include <unordered_map>
#include <vector>

struct TrieNode {
    std::unordered_map<char, TrieNode*> children;
    bool is_end_of_word;
    TrieNode() : is_end_of_word(false) {}
};

struct NaryTreeNode {
    int data;
    std::vector<NaryTreeNode*> children;
    NaryTreeNode(int val) : data(val) {}
};

int main() {
    TrieNode trie_root;
    NaryTreeNode nary_root(1);
    std::cout << "Trie and N-ary root nodes created." << std::endl;
    return 0;
}
