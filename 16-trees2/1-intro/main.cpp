// Basic BST Node - C++ Example

#include <iostream>

struct BSTNode {
    int data;
    BSTNode* left;
    BSTNode* right;
    BSTNode(int val) : data(val), left(nullptr), right(nullptr) {}
};

BSTNode* insert(BSTNode* root, int key) {
    if (!root) return new BSTNode(key);
    if (key < root->data)
        root->left = insert(root->left, key);
    else
        root->right = insert(root->right, key);
    return root;
}

int main() {
    BSTNode* root = nullptr;
    int vals[] = {10,5,15,3,7,13,17};
    for (int val : vals) {
        root = insert(root, val);
    }
    std::cout << "BST constructed with root: " << root->data << std::endl;
    return 0;
}
