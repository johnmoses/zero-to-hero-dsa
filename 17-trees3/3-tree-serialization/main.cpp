// Tree Serialization and Deserialization - C++ Example

#include <iostream>
#include <sstream>
#include <string>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int v) : val(v), left(nullptr), right(nullptr) {}
};

void serialize(TreeNode* root, std::ostringstream& out) {
    if (!root) {
        out << "#,";
        return;
    }
    out << root->val << ",";
    serialize(root->left, out);
    serialize(root->right, out);
}

TreeNode* deserialize(std::istringstream& in) {
    std::string val;
    if (!getline(in, val, ',')) return nullptr;
    if (val == "#") return nullptr;
    
    TreeNode* node = new TreeNode(std::stoi(val));
    node->left = deserialize(in);
    node->right = deserialize(in);
    return node;
}

int main() {
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->right->left = new TreeNode(4);
    root->right->right = new TreeNode(5);

    std::ostringstream out;
    serialize(root, out);
    std::string serialized = out.str();

    std::cout << "Serialized tree: " << serialized << std::endl;

    std::istringstream in(serialized);
    TreeNode* new_root = deserialize(in);
    std::cout << "Deserialized root value: " << new_root->val << std::endl;

    return 0;
}
