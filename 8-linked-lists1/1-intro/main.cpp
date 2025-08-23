// Linked List Introduction - C++ Example

#include <iostream>

struct Node {
    int data;
    Node* next;
    Node(int val) : data(val), next(nullptr) {}
};

int main() {
    Node* node1 = new Node(1);
    Node* node2 = new Node(2);
    node1->next = node2;

    Node* current = node1;
    while (current != nullptr) {
        std::cout << current->data << std::endl;
        current = current->next;
    }

    // Free memory
    delete node2;
    delete node1;
    return 0;
}
