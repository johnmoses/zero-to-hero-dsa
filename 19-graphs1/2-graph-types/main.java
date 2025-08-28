// Graph Types - Java Example

import java.util.*;

class GraphTypes {
    public static void main(String[] args) {
        Map<String, List<String>> directedGraph = new HashMap<>();
        directedGraph.put("A", Arrays.asList("B"));
        directedGraph.put("B", Arrays.asList("C"));
        directedGraph.put("C", Arrays.asList());

        Map<String, List<AbstractMap.SimpleEntry<String, Integer>>> weightedGraph = new HashMap<>();
        weightedGraph.put("A", Arrays.asList(new AbstractMap.SimpleEntry<>("B", 4), new AbstractMap.SimpleEntry<>("C", 3)));
        weightedGraph.put("B", Arrays.asList(new AbstractMap.SimpleEntry<>("A", 4), new AbstractMap.SimpleEntry<>("C", 1)));
        weightedGraph.put("C", Arrays.asList(new AbstractMap.SimpleEntry<>("A", 3), new AbstractMap.SimpleEntry<>("B", 1)));

        System.out.println("Directed graph edges from A: " + directedGraph.get("A"));
        System.out.print("Weighted edges from A: ");
        for (AbstractMap.SimpleEntry<String, Integer> entry : weightedGraph.get("A")) {
            System.out.print("(" + entry.getKey() + ", " + entry.getValue() + ") ");
        }
        System.out.println();
    }
}
