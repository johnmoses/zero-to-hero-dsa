// Recursive Tree Algorithms - Java Example

class TreeNode {
    int data;
    TreeNode left, right;
    TreeNode(int data) {
        this.data = data;
        left = right = null;
    }
}

public class RecursiveTreeAlgorithms {

    public static int treeHeight(TreeNode node) {
        if (node == null) return 0;
        int leftHeight = treeHeight(node.left);
        int rightHeight = treeHeight(node.right);
        return Math.max(leftHeight, rightHeight) + 1;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);

        System.out.println("Tree height: " + treeHeight(root));
    }
}
