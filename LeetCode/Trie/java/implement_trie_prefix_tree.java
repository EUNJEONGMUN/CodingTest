package LeetCode.Trie.java;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

/*
https://leetcode.com/problems/implement-trie-prefix-tree/description/?envType=study-plan-v2&envId=top-interview-150
 */

public class implement_trie_prefix_tree {
    public static void main(String[] args) {
        Trie trie = new Trie();
        List<String> op = List.of("insert","insert","insert","insert","insert","insert","search","search");
        List<String> words = List.of("app", "apple","beer","add","jam","rental","apps","app");
        for (int i=0; i<op.size(); i++) {
            if (op.get(i).equals("insert")) {
                trie.insert(words.get(i));
            } else if (op.get(i).equals("search")) {
                System.out.println(trie.search(words.get(i)));
            } else {
                System.out.println(trie.startsWith(words.get(i)));
            }
        }
    }
}

class Trie {
    Node head;

    public Trie() {
        head = new Node();
    }

    public void insert(String word) {
        Node curr = head;
        for (char c : word.toCharArray()) {
            if (!curr.children.containsKey(c)) {
                curr.children.put(c, new Node(c));
            }
            curr = curr.children.get(c);
        }
        curr.data = word;
    }

    public boolean search(String word) {
        Node curr = head;
        for (char c : word.toCharArray()) {
            if (!curr.children.containsKey(c)) {
                return false;
            }
            curr = curr.children.get(c);
        }
        return curr.data.equals(word);
    }

    public boolean startsWith(String prefix) {
        Node curr = head;

        for (char c : prefix.toCharArray()) {
            if (!curr.children.containsKey(c)) {
                return false;
            }
            curr = curr.children.get(c);
        }
        return true;
    }
}

class Node {
    char key;
    String data = "";
    Map<Character, Node> children = new HashMap<>();

    public Node() {

    }

    public Node(char c) {
        this.key = c;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */