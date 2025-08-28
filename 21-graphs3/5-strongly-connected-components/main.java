// Strongly Connected Components - Kosaraju's Algorithm - Java Example

import java.util.*;

class KosarajuSCC {

    public static void dfs(Map<Integer, List<Integer>> graph, int v, Set<Integer> visited, Stack<Integer> stack) {
        visited.add(v);
        for (int nbr : graph.getOrDefault(v, Collections.emptyList())) {
            if (!visited.contains(nbr)) {
                dfs(graph, nbr, visited, stack);
            }
        }
        stack.push(v);
    }

    public static void dfsCollect(Map<Integer, List<Integer>> graph, int v, Set<Integer> visited, List<Integer> component) {
        visited.add(v);
        component.add(v);
        for (int nbr : graph.getOrDefault(v, Collections.emptyList())) {
            if (!visited.contains(nbr)) {
                dfsCollect(graph, nbr, visited, component);
            }
        }
    }

    public static Map<Integer, List<Integer>> reverseGraph(Map<Integer, List<Integer>> graph) {
        Map<Integer, List<Integer>> rev = new HashMap<>();
        for (int u : graph.keySet()) {
            for (int v : graph.get(u)) {
                rev.computeIfAbsent(v, k -> new ArrayList<>()).add(u);
            }
        }
        return rev;
    }

    public static List<List<Integer>> kosarajuSCC(Map<Integer, List<Integer>> graph) {
        Set<Integer> visited = new HashSet<>();
        Stack<Integer> stack = new Stack<>();

        for (int v : graph.keySet()) {
            if (!visited.contains(v)) dfs(graph, v, visited, stack);
        }

        Map<Integer, List<Integer>> rev = reverseGraph(graph);
        visited.clear();
        List<List<Integer>> sccs = new ArrayList<>();

        while (!stack.isEmpty()) {
            int v = stack.pop();
            if (!visited.contains(v)) {
                List<Integer> component = new ArrayList<>();
                dfsCollect(rev, v, visited, component);
                sccs.add(component);
            }
        }
        return sccs;
    }

    public static void main(String[] args) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        graph.put(0, Arrays.asList(1));
        graph.put(1, Arrays.asList(2));
        graph.put(2, Arrays.asList(0, 3));
        graph.put(3, Arrays.asList(4));
        graph.put(4, Collections.emptyList());

        List<List<Integer>> sccs = kosarajuSCC(graph);
        System.out.println("Strongly connected components:");
        for (List<Integer> component : sccs) {
            System.out.println(component);
        }
    }
}
