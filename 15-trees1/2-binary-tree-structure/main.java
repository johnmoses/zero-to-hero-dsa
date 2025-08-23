// Binary Tree Structure - Java Example

class TreeNode {
    int data;
    TreeNode left, right;
    TreeNode(int data) {
        this.data = data;
        left = right = null;
    }
}

public class BinaryTreeStructure {

    public static boolean isFullBinaryTree(TreeNode node) {
        if (node == null) return true;
        if ((node.left == null) != (node.right == null)) return false;
        return isFullBinaryTree(node.left) && isFullBinaryTree(node.right);
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);

        System.out.println("Is full binary tree: " + isFullBinaryTree(root));
    }
}
