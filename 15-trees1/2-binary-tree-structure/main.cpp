// Binary Tree Structure - C++ Example

#include <iostream>
using namespace std;

struct TreeNode {
    int data;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int val) : data(val), left(nullptr), right(nullptr) {}
};

bool isFullBinaryTree(TreeNode* node) {
    if (!node) return true;
    if ((node->left == nullptr) != (node->right == nullptr)) return false;
    return isFullBinaryTree(node->left) && isFullBinaryTree(node->right);
}

int main() {
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);

    cout << "Is full binary tree: " << (isFullBinaryTree(root) ? "true" : "false") << endl;
    return 0;
}
