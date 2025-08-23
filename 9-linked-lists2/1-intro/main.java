// Advanced Linked Lists Introduction - Java Example

class DNode {
    int data;
    DNode prev, next;
    DNode(int data) {
        this.data = data;
        this.prev = this.next = null;
    }
}

class CDNode {
    int data;
    CDNode next;
    CDNode(int data) {
        this.data = data;
        this.next = null;
    }
}

public class AdvancedLinkedListsIntro {
    public static void main(String[] args) {
        // Doubly linked list
        DNode node1 = new DNode(1);
        DNode node2 = new DNode(2);
        node1.next = node2;
        node2.prev = node1;

        // Circular linked list
        CDNode node3 = new CDNode(3);
        CDNode node4 = new CDNode(4);
        node3.next = node4;
        node4.next = node3; // circular link
    }
}
