// Advanced Graph Algorithms Introduction - Java Example

import java.util.*;

class GraphIntroAdvanced {
    public static void main(String[] args) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        graph.put(0, Arrays.asList(1, 2));
        graph.put(1, Arrays.asList(0));
        graph.put(2, Arrays.asList(0, 3));
        graph.put(3, Arrays.asList(2));

        System.out.println("Graph vertices: " + graph.keySet());
        System.out.println("Graph edges from 0: " + graph.get(0));
    }
}
