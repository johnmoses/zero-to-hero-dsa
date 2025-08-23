// Linked List Problems - C++ Example

#include <iostream>

struct Node {
    int data;
    Node* next;
    Node(int val) : data(val), next(nullptr) {}
};

Node* reverseList(Node* head) {
    Node* prev = nullptr;
    Node* curr = head;
    while (curr) {
        Node* nxt = curr->next;
        curr->next = prev;
        prev = curr;
        curr = nxt;
    }
    return prev;
}

int main() {
    Node* head = new Node(1);
    head->next = new Node(2);
    head->next->next = new Node(3);

    Node* reversed = reverseList(head);
    Node* current = reversed;
    while (current) {
        std::cout << current->data << std::endl;
        current = current->next;
    }

    // Memory cleanup omitted for brevity
    return 0;
}
