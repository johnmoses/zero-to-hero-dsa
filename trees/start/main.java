/**
 * Binary Trees

Given some items, A, B, C, and so on, write a basic binary tree to demonstrate it's core functionalities
 */

class Node {
    String data;
    Node left;
    Node right;

    public Node(String data) {
        this.data = data;
        this.left = left;
        this.right = right;
    }
}

public class main {
    public static void main(String[] args) {
        System.out.println("Trees");

        // Instantiate the nodes
        Node a = new Node("A");
        Node b = new Node("B");
        Node c = new Node("C");

        // Assign values
        a.left = b;
        a.right = c;
        System.out.print(a.right.data + " ");
    }
}