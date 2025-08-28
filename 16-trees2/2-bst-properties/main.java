// BST Property Check - Java Example

class BSTNode {
    int data;
    BSTNode left, right;
    BSTNode(int data) {
        this.data = data;
        left = right = null;
    }
}

class BSTProperties {

    public static boolean isBST(BSTNode root, int minVal, int maxVal) {
        if (root == null) return true;
        if (root.data <= minVal || root.data >= maxVal) return false;
        return isBST(root.left, minVal, root.data) && isBST(root.right, root.data, maxVal);
    }

    public static void main(String[] args) {
        BSTNode root = new BSTNode(10);
        root.left = new BSTNode(5);
        root.right = new BSTNode(15);
        root.left.left = new BSTNode(3);
        root.left.right = new BSTNode(7);

        System.out.println("Is BST: " + isBST(root, Integer.MIN_VALUE, Integer.MAX_VALUE));
    }
}
