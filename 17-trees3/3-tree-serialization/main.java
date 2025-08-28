// Tree Serialization and Deserialization - Java Example

import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int val) {
        this.val = val;
    }
}

class TreeSerialization {

    // Serializes a tree to a single string.
    public String serialize(TreeNode root) {
        if (root == null) return "#,";
        return root.val + "," + serialize(root.left) + serialize(root.right);
    }

    // Deserializes encoded data to tree.
    public TreeNode deserialize(Queue<String> nodes) {
        String val = nodes.poll();
        if (val.equals("#")) return null;
        TreeNode node = new TreeNode(Integer.parseInt(val));
        node.left = deserialize(nodes);
        node.right = deserialize(nodes);
        return node;
    }

    public TreeNode deserialize(String data) {
        String[] parts = data.split(",");
        Queue<String> nodes = new LinkedList<>(Arrays.asList(parts));
        return deserialize(nodes);
    }

    public static void main(String[] args) {
        TreeSerialization codec = new TreeSerialization();

        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.right.left = new TreeNode(4);
        root.right.right = new TreeNode(5);

        String serialized = codec.serialize(root);
        System.out.println("Serialized tree: " + serialized);

        TreeNode newRoot = codec.deserialize(serialized);
        System.out.println("Deserialized root value: " + newRoot.val);
    }
}
