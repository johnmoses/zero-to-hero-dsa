// Basic BST Node - Java Example

class BSTNode {
    int data;
    BSTNode left, right;
    BSTNode(int data) {
        this.data = data;
        left = right = null;
    }
}

public class BSTIntro {
    public static BSTNode insert(BSTNode root, int key) {
        if (root == null) return new BSTNode(key);
        if (key < root.data)
            root.left = insert(root.left, key);
        else
            root.right = insert(root.right, key);
        return root;
    }

    public static void main(String[] args) {
        BSTNode root = null;
        int[] vals = {10, 5, 15, 3, 7, 13, 17};
        for (int val : vals) {
            root = insert(root, val);
        }
        System.out.println("BST constructed with root: " + root.data);
    }
}
