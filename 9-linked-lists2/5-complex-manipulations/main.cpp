// Complex Linked List Manipulations - C++ Example

#include <iostream>

struct DNode {
    int data;
    DNode* prev;
    DNode* next;
    DNode(int val) : data(val), prev(nullptr), next(nullptr) {}
};

DNode* reverseDoublyLinkedList(DNode* head) {
    DNode* current = head;
    DNode* prevNode = nullptr;
    while (current) {
        prevNode = current->prev;
        current->prev = current->next;
        current->next = prevNode;
        current = current->prev;
    }
    if (prevNode) {
        head = prevNode->prev;
    }
    return head;
}

int main() {
    DNode* head = new DNode(1);
    DNode* node2 = new DNode(2);
    DNode* node3 = new DNode(3);
    head->next = node2;
    node2->prev = head;
    node2->next = node3;
    node3->prev = node2;

    head = reverseDoublyLinkedList(head);

    DNode* curr = head;
    while (curr) {
        std::cout << curr->data << std::endl;
        curr = curr->next;
    }

    // Memory cleanup omitted for brevity
    return 0;
}
