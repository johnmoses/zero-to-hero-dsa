// Tree Node Definition - C++ Example

#include <iostream>

struct TreeNode {
    int data;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int val) : data(val), left(nullptr), right(nullptr) {}
};

int main() {
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);

    std::cout << "Root node: " << root->data << std::endl;
    std::cout << "Left child: " << root->left->data << std::endl;
    std::cout << "Right child: " << root->right->data << std::endl;

    return 0;
}
