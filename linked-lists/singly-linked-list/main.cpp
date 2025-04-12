/*
Singly Linked Lists

Given some nodes with values 20, 30, 40, design a fully functional singly linked list with the following operations:
    - get value of node
    - add node at head
    - add node at tail
    - add node at index
    - delete node at index
    - traverse and display nodes
*/
#include <iostream>

class Node {
public:
    int data;
    Node* next;

    Node(int data) {
        this->data = data;
        this->next = nullptr;
    }
};

class LinkedList {
public:
    Node* head;

    LinkedList() {
        head = nullptr;
    }

    int getValue(int index) {
        Node* current = head;
        int count = 0;
        while (current != nullptr) {
            if (count == index) {
                return current->data;
            }
            count++;
            current = current->next;
        }
        return -1;
    }

    void addAtHead(int data) {
        Node* newNode = new Node(data);
        newNode->next = head;
        head = newNode;
    }

    void addAtTail(int data) {
        Node* newNode = new Node(data);
        if (head == nullptr) {
            head = newNode;
            return;
        }
        Node* current = head;
        while (current->next != nullptr) {
            current = current->next;
        }
        current->next = newNode;
    }

    void addAtIndex(int data, int index) {
        if (index == 0) {
            addAtHead(data);
            return;
        }
        Node* newNode = new Node(data);
        Node* current = head;
        int count = 0;
        while (current != nullptr && count < index - 1) {
            current = current->next;
            count++;
        }
        if (current == nullptr) return;
        newNode->next = current->next;
        current->next = newNode;
    }

    void deleteAtIndex(int index) {
        if (head == nullptr) return;
        if (index == 0) {
            Node* temp = head;
            head = head->next;
            delete temp;
            return;
        }
        Node* current = head;
        int count = 0;
        while (current != nullptr && count < index - 1) {
            current = current->next;
            count++;
            if (current == nullptr || current->next == nullptr) return;
            Node* temp = current->next;
            current->next = temp->next;
            delete temp;
        }
        if (current == nullptr) return;
        Node* temp = current->next;
        current->next = temp->next;
        delete temp;
    }
    void traverse() {
        Node* current = head;
        while (current != nullptr) {
            std::cout << current->data << " ";
            current = current->next;
        }
        std::cout << std::endl;
    }
    ~LinkedList() {
        Node* current = head;
        while (current != nullptr) {
            Node* temp = current;
            current = current->next;
            delete temp;
        }
    }
    void display() {
        Node* current = head;
        while (current != nullptr) {
            std::cout << current->data << " ";
            current = current->next;
        }
        std::cout << std::endl;
    }
    void displayReverse(Node* node) {
        if (node == nullptr) return;
        displayReverse(node->next);
        std::cout << node->data << " ";
    }
};


int main() {
    LinkedList list;
    list.addAtHead(20);
    list.addAtHead(30);
    list.addAtHead(40);
    list.addAtTail(50);
    list.addAtIndex(60, 2);
    list.deleteAtIndex(2);
    list.traverse();
    list.display();
    list.displayReverse(list.head);
    return 0;
}
