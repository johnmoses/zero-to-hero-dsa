// Fast and Slow Pointers - C++ Example

#include <iostream>

struct Node {
    int data;
    Node* next;
    Node(int val) : data(val), next(nullptr) {}
};

bool hasCycle(Node* head) {
    Node* slow = head;
    Node* fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) return true;
    }
    return false;
}

int main() {
    Node* head = new Node(1);
    head->next = new Node(2);
    head->next->next = new Node(3);
    head->next->next->next = head->next; // create cycle

    std::cout << "Cycle detected: " << (hasCycle(head) ? "true" : "false") << std::endl;

    // Note: memory leak due to cycle, omitted for brevity
    return 0;
}
