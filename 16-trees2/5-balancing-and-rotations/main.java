// Tree Rotations - Java Example

class TreeNode {
    int key;
    TreeNode left, right;
    TreeNode(int key) {
        this.key = key;
        left = right = null;
    }
}

class TreeRotations {

    public static TreeNode leftRotate(TreeNode x) {
        TreeNode y = x.right;
        x.right = y.left;
        y.left = x;
        return y;
    }

    public static TreeNode rightRotate(TreeNode y) {
        TreeNode x = y.left;
        y.left = x.right;
        x.right = y;
        return x;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(10);
        root.right = new TreeNode(20);
        root = leftRotate(root);
        System.out.println("Root after left rotation: " + root.key);
    }
}
