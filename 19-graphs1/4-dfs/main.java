// Depth-First Search (DFS) - Java Example

import java.util.*;

class DFSGraph {
    public static void dfs(Map<String, List<String>> graph, String node, Set<String> visited) {
        visited.add(node);
        System.out.print(node + " ");
        for (String neighbor : graph.getOrDefault(node, Collections.emptyList())) {
            if (!visited.contains(neighbor)) {
                dfs(graph, neighbor, visited);
            }
        }
    }

    public static void main(String[] args) {
        Map<String, List<String>> graph = new HashMap<>();
        graph.put("A", Arrays.asList("B", "C"));
        graph.put("B", Arrays.asList("D"));
        graph.put("C", Arrays.asList("D"));
        graph.put("D", Collections.emptyList());

        Set<String> visited = new HashSet<>();
        System.out.print("DFS traversal starting from A: ");
        dfs(graph, "A", visited);
    }
}
