// BST Property Check - C++ Example

#include <iostream>
#include <climits>

struct BSTNode {
    int data;
    BSTNode* left;
    BSTNode* right;
    BSTNode(int val) : data(val), left(nullptr), right(nullptr) {}
};

bool isBST(BSTNode* root, int minVal=INT_MIN, int maxVal=INT_MAX) {
    if (!root) return true;
    if (root->data <= minVal || root->data >= maxVal) return false;
    return isBST(root->left, minVal, root->data) && isBST(root->right, root->data, maxVal);
}

int main() {
    BSTNode* root = new BSTNode(10);
    root->left = new BSTNode(5);
    root->right = new BSTNode(15);
    root->left->left = new BSTNode(3);
    root->left->right = new BSTNode(7);

    std::cout << "Is BST: " << (isBST(root) ? "true" : "false") << std::endl;
    return 0;
}
