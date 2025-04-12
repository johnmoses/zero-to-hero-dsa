/**
 * 
 * Singly Linked Lists

Given some nodes with values 20, 30, 40, design a fully functional singly linked list with the following operations:
    - get value of node
    - add node at head
    - add node at tail
    - add node at index
    - delete node at index
    - traverse and display nodes
 */
class Node {
    int data;
    Node next;
    
    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

class main {
    Node head;
    
    // Get value at index
    public int get(int index) {
        Node current = head;
        int count = 0;
        
        while (current != null && count < index) {
            current = current.next;
            count++;
        }
        
        return current != null ? current.data : -1;

    }
    
    // Add node at head
    public void addAtHead(int data) {
        Node newNode = new Node(data);
        newNode.next = head;
        head = newNode;
    }

    
    // Add node at tail
    public void addAtTail(int data) {
        if (head == null) {
            head = new Node(data);
            return;
        }
        
        Node current = head;
        while (current.next != null) {
            current = current.next;
        }
        current.next = new Node(data);

    }
    
    // Add node at index
    public void addAtIndex(int index, int data) {
        if (index == 0) {
            addAtHead(data);
            return;
        }
        
        Node current = head;
        for (int i = 0; i < index-1 && current != null; i++) {
            current = current.next;
        }

        
        if (current != null) {
            Node newNode = new Node(data);
            newNode.next = current.next;
            current.next = newNode;
        }
    }

    
    // Delete node at index 
    public void deleteAtIndex(int index) {
        if (head == null || index < 0) return;
        
        if (index == 0) {
            head = head.next;
            return;
        }
        
        Node current = head;
        for (int i = 0; i < index-1 && current.next != null; i++) {
            current = current.next;
        }

        
        if (current.next != null) {
            current.next = current.next.next;
        }
    }

    
    // Display all nodes
    public void display() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " -> ");
            current = current.next;
        }
        System.out.println("null");
    }

    public static void main(String[] args) {
        main list = new main();
        list.addAtHead(20);
        list.addAtTail(30);
        list.addAtTail(40);
        list.addAtIndex(1, 25);
        list.display();
        System.out.println("Value at index 1: " + list.get(1));
        list.deleteAtIndex(1);
        list.display();
    }
}