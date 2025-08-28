// Doubly Linked List - Java Example

class DNode {
    int data;
    DNode prev, next;
    DNode(int data) {
        this.data = data;
        this.prev = this.next = null;
    }
}

class DoublyLinkedList {
    DNode head;

    public void insertAtHead(int data) {
        DNode newNode = new DNode(data);
        newNode.next = head;
        if (head != null) {
            head.prev = newNode;
        }
        head = newNode;
    }

    public void printForward() {
        DNode curr = head;
        while (curr != null) {
            System.out.print(curr.data + " ");
            curr = curr.next;
        }
        System.out.println();
    }

    public void printBackward() {
        if (head == null) return;
        DNode curr = head;
        while (curr.next != null) {
            curr = curr.next;
        }
        while (curr != null) {
            System.out.print(curr.data + " ");
            curr = curr.prev;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        DoublyLinkedList dll = new DoublyLinkedList();
        dll.insertAtHead(3);
        dll.insertAtHead(2);
        dll.insertAtHead(1);
        dll.printForward();
        dll.printBackward();
    }
}
