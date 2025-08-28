// Connected Components - Java Example (Undirected graph)

import java.util.*;

class ConnectedComponents {

    public static void dfs(Map<Integer, List<Integer>> graph, int node, Set<Integer> visited, List<Integer> component) {
        visited.add(node);
        component.add(node);
        for (int neighbor : graph.getOrDefault(node, Collections.emptyList())) {
            if (!visited.contains(neighbor)) {
                dfs(graph, neighbor, visited, component);
            }
        }
    }

    public static List<List<Integer>> connectedComponents(Map<Integer, List<Integer>> graph) {
        Set<Integer> visited = new HashSet<>();
        List<List<Integer>> components = new ArrayList<>();

        for (int node : graph.keySet()) {
            if (!visited.contains(node)) {
                List<Integer> component = new ArrayList<>();
                dfs(graph, node, visited, component);
                components.add(component);
            }
        }
        return components;
    }

    public static void main(String[] args) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        graph.put(0, Arrays.asList(1));
        graph.put(1, Arrays.asList(0, 2));
        graph.put(2, Arrays.asList(1));
        graph.put(3, Arrays.asList());

        List<List<Integer>> comps = connectedComponents(graph);
        System.out.println("Connected Components:");
        for (List<Integer> comp : comps) {
            System.out.println(comp);
        }
    }
}
