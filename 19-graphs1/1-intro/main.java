// Graph Introduction - Java Example

import java.util.*;

public class GraphIntro {
    public static void main(String[] args) {
        Map<String, List<String>> graph = new HashMap<>();
        graph.put("A", Arrays.asList("B", "C"));
        graph.put("B", Arrays.asList("A", "D"));
        graph.put("C", Arrays.asList("A", "D"));
        graph.put("D", Arrays.asList("B", "C"));

        System.out.println("Neighbors of node A: " + graph.get("A"));
    }
}
