/*
Singly Linked Lists

Given some nodes, 20, 30, 40, write a basic linked list to link the nodes, traverse and display the nodes in order.
*/
#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* next;
};

int main() {
    Node* head = NULL;
    Node* second = NULL;
    Node* third = NULL;

    head = new Node();
    second = new Node();
    third = new Node();

    head->data = 20;
    head->next = second;

    second->data = 30;
    second->next = third;

    third->data = 40;
    third->next = NULL;

    Node* current = head;
    while (current != NULL) {
        cout << current->data << " ";
        current = current->next;
    }

    return 0;
}
