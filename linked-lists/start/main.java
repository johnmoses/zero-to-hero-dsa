/**
 * Singly Linked Lists

Given some nodes, 20, 30, 40, write a basic linked list to link the nodes, traverse and display the nodes in order.
 */
class Node {
    int data;
    Node next;
    
    public Node(int data) {
        this.data = data;
        this.next = null;
    }

}

public class main {
    private Node head;
    
    public void insert(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
        } else {
            Node current = head;
            while (current.next != null) {
                current = current.next;
            }
            current.next = newNode;
        }

    }
    
    public void display() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " ");
            current = current.next;
        }
    }


    public static void main(String[] args) {
        main ll = new main();
        ll.insert(20);
        ll.insert(30); 
        ll.insert(40);
        ll.display();
    }
}