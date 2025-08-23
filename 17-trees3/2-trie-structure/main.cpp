// Trie Structure - C++ Example

#include <iostream>
#include <unordered_map>
using namespace std;

struct TrieNode {
    unordered_map<char, TrieNode*> children;
    bool is_end_of_word;
    TrieNode() : is_end_of_word(false) {}
};

class Trie {
    TrieNode* root;
public:
    Trie() { root = new TrieNode(); }

    void insert(const string& word) {
        TrieNode* curr = root;
        for (char c : word) {
            if (curr->children.find(c) == curr->children.end())
                curr->children[c] = new TrieNode();
            curr = curr->children[c];
        }
        curr->is_end_of_word = true;
    }

    bool search(const string& word) {
        TrieNode* curr = root;
        for (char c : word) {
            if (curr->children.find(c) == curr->children.end())
                return false;
            curr = curr->children[c];
        }
        return curr->is_end_of_word;
    }
};

int main() {
    Trie trie;
    trie.insert("apple");
    cout << "Search 'apple': " << (trie.search("apple") ? "true" : "false") << endl;
    cout << "Search 'app': " << (trie.search("app") ? "true" : "false") << endl;
    return 0;
}
