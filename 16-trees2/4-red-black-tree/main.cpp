// Red-Black Tree Node - C++ Partial Example

enum Color {RED, BLACK};

struct RBNode {
    int key;
    Color color;
    RBNode* left;
    RBNode* right;
    RBNode* parent;

    RBNode(int key) : key(key), color(RED), left(nullptr), right(nullptr), parent(nullptr) {}
};

// Further implementation includes rebalancing and rotations after insert/delete.
