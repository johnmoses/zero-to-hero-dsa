// Singly Linked List - C++ Example

#include <iostream>

struct Node {
    int data;
    Node* next;
    Node(int val) : data(val), next(nullptr) {}
};

class SinglyLinkedList {
    Node* head;
public:
    SinglyLinkedList() : head(nullptr) {}

    void insertAtBeginning(int data) {
        Node* newNode = new Node(data);
        newNode->next = head;
        head = newNode;
    }

    void printList() {
        Node* current = head;
        while (current) {
            std::cout << current->data << std::endl;
            current = current->next;
        }
    }

    ~SinglyLinkedList() {
        Node* current = head;
        while (current) {
            Node* temp = current;
            current = current->next;
            delete temp;
        }
    }
};

int main() {
    SinglyLinkedList sll;
    sll.insertAtBeginning(3);
    sll.insertAtBeginning(2);
    sll.insertAtBeginning(1);
    sll.printList();
    return 0;
}
