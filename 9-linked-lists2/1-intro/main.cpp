// Advanced Linked Lists Introduction - C++ Example

#include <iostream>

struct DNode {
    int data;
    DNode* prev;
    DNode* next;
    DNode(int val) : data(val), prev(nullptr), next(nullptr) {}
};

struct CDNode {
    int data;
    CDNode* next;
    CDNode(int val) : data(val), next(nullptr) {}
};

int main() {
    // Doubly linked list
    DNode* node1 = new DNode(1);
    DNode* node2 = new DNode(2);
    node1->next = node2;
    node2->prev = node1;

    // Circular linked list
    CDNode* node3 = new CDNode(3);
    CDNode* node4 = new CDNode(4);
    node3->next = node4;
    node4->next = node3; // circular link

    // Cleanup omitted for brevity
    return 0;
}
