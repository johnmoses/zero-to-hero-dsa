/*
Binary Trees

Given some items, A, B, C, and so on, write a basic binary tree to demonstrate it's core functionalities
*/

#include <iostream>

using namespace std;

class Node {
    public:
        string data;
        Node* left;
        Node* right;
};

int main() {
    cout << "Tree:" << " ";

    // Initialize nodes
    Node* a = NULL;
    Node* b = NULL;
    Node* c = NULL;
    
    // Insantiate nodes
    a = new Node();
    b = new Node();
    c = new Node();

    // Assign values
    a->data = "A";
    a->left = b;
    a->right = c;

    b->data = "B";

    c->data = "C";

    cout << a->right->data << " ";

    return 0;
}