// Introduction to Trie and N-ary Tree Nodes - Java Example

import java.util.HashMap;
import java.util.ArrayList;

class TrieNode {
    HashMap<Character, TrieNode> children = new HashMap<>();
    boolean isEndOfWord = false;
}

class NaryTreeNode {
    int data;
    ArrayList<NaryTreeNode> children = new ArrayList<>();
    NaryTreeNode(int data) {
        this.data = data;
    }
}

class Trees3Intro {
    public static void main(String[] args) {
        TrieNode trieRoot = new TrieNode();
        NaryTreeNode naryRoot = new NaryTreeNode(1);
        System.out.println("Trie and N-ary root nodes created.");
    }
}
