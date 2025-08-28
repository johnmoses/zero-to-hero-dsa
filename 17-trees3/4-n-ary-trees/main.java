// N-ary Tree Implementation and Level-Order Traversal - Java Example

import java.util.*;

class NaryTreeNode {
    int data;
    List<NaryTreeNode> children;

    NaryTreeNode(int data) {
        this.data = data;
        this.children = new ArrayList<>();
    }
}

class NaryTreeTraversal {
    public static void levelOrder(NaryTreeNode root) {
        if (root == null) return;
        Queue<NaryTreeNode> queue = new LinkedList<>();
        queue.add(root);

        while (!queue.isEmpty()) {
            NaryTreeNode node = queue.poll();
            System.out.print(node.data + " ");
            for (NaryTreeNode child : node.children) {
                queue.add(child);
            }
        }
    }

    public static void main(String[] args) {
        NaryTreeNode root = new NaryTreeNode(1);
        NaryTreeNode c1 = new NaryTreeNode(2);
        NaryTreeNode c2 = new NaryTreeNode(3);
        NaryTreeNode c3 = new NaryTreeNode(4);

        root.children = Arrays.asList(c1, c2, c3);
        c1.children = Arrays.asList(new NaryTreeNode(5), new NaryTreeNode(6));

        System.out.print("Level order traversal of N-ary tree: ");
        levelOrder(root);
    }
}
