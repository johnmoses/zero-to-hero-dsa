// 2 Doubly Linked Lists - C++ example

#include <iostream>

int main() {
    // TODO: Add code
    return 0;
}
// Doubly Linked List - C++ Example

#include <iostream>

struct DNode {
    int data;
    DNode* prev;
    DNode* next;
    DNode(int val) : data(val), prev(nullptr), next(nullptr) {}
};

class DoublyLinkedList {
    DNode* head;
public:
    DoublyLinkedList() : head(nullptr) {}

    void insertAtHead(int data) {
        DNode* newNode = new DNode(data);
        newNode->next = head;
        if (head) head->prev = newNode;
        head = newNode;
    }

    void printForward() {
        DNode* curr = head;
        while (curr) {
            std::cout << curr->data << " ";
            curr = curr->next;
        }
        std::cout << std::endl;
    }

    void printBackward() {
        DNode* curr = head;
        if (!curr) return;
        while (curr->next) curr = curr->next;

        while (curr) {
            std::cout << curr->data << " ";
            curr = curr->prev;
        }
        std::cout << std::endl;
    }
};

int main() {
    DoublyLinkedList dll;
    dll.insertAtHead(3);
    dll.insertAtHead(2);
    dll.insertAtHead(1);

    dll.printForward();
    dll.printBackward();

    return 0;
}
