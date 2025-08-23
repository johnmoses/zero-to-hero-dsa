// Red-Black Tree Node - Java Partial Example

enum Color { RED, BLACK; }

class RBNode {
    int key;
    Color color;
    RBNode left, right, parent;

    RBNode(int key) {
        this.key = key;
        this.color = Color.RED;
        left = right = parent = null;
    }
}

// Full red-black operations involve insert/delete fixup and rotations.
