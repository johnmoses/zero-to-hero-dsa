// Tree Node Definition - Java Example

class TreeNode {
    int data;
    TreeNode left, right;
    TreeNode(int data) {
        this.data = data;
        left = right = null;
    }
}

public class TreeIntro {
    public static void main(String[] args) {
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);

        System.out.println("Root node: " + root.data);
        System.out.println("Left child: " + root.left.data);
        System.out.println("Right child: " + root.right.data);
    }
}
