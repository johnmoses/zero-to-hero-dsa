// Linked List Introduction - Java Example

class Node {
    int data;
    Node next;
    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

class LinkedListIntro {
    public static void main(String[] args) {
        Node node1 = new Node(1);
        Node node2 = new Node(2);
        node1.next = node2;

        Node current = node1;
        while (current != null) {
            System.out.println(current.data);
            current = current.next;
        }
    }
}
