// Tree Rotations - C++ Example

#include <iostream>

struct TreeNode {
    int key;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int k) : key(k), left(nullptr), right(nullptr) {}
};

TreeNode* leftRotate(TreeNode* x) {
    TreeNode* y = x->right;
    x->right = y->left;
    y->left = x;
    return y;
}

TreeNode* rightRotate(TreeNode* y) {
    TreeNode* x = y->left;
    y->left = x->right;
    x->right = y;
    return x;
}

int main() {
    TreeNode* root = new TreeNode(10);
    root->right = new TreeNode(20);
    root = leftRotate(root);
    std::cout << "Root after left rotation: " << root->key << std::endl;
    return 0;
}
