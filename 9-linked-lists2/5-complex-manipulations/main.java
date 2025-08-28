// Complex Linked List Manipulations - Java Example

class DNode {
    int data;
    DNode prev, next;
    DNode(int data) {
        this.data = data;
        this.prev = this.next = null;
    }
}

class ComplexManipulations {

    public static DNode reverseDoublyLinkedList(DNode head) {
        DNode current = head;
        DNode prevNode = null;
        while (current != null) {
            prevNode = current.prev;
            current.prev = current.next;
            current.next = prevNode;
            current = current.prev;
        }
        if (prevNode != null)
            head = prevNode.prev;
        return head;
    }

    public static void main(String[] args) {
        DNode head = new DNode(1);
        DNode node2 = new DNode(2);
        DNode node3 = new DNode(3);
        head.next = node2;
        node2.prev = head;
        node2.next = node3;
        node3.prev = node2;

        head = reverseDoublyLinkedList(head);
        DNode curr = head;
        while (curr != null) {
            System.out.println(curr.data);
            curr = curr.next;
        }
    }
}
