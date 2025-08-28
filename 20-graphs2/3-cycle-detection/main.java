// Cycle Detection in Directed Graph - Java Example

import java.util.*;

class CycleDetection {

    private static boolean isCyclicUtil(Map<Integer, List<Integer>> graph, int v,
        Set<Integer> visited, Set<Integer> recStack) {

        visited.add(v);
        recStack.add(v);

        for (int neighbor : graph.getOrDefault(v, Collections.emptyList())) {
            if (!visited.contains(neighbor)) {
                if (isCyclicUtil(graph, neighbor, visited, recStack)) {
                    return true;
                }
            }
            else if (recStack.contains(neighbor)) {
                return true;
            }
        }
        recStack.remove(v);
        return false;
    }

    public static boolean isCyclic(Map<Integer, List<Integer>> graph) {
        Set<Integer> visited = new HashSet<>();
        Set<Integer> recStack = new HashSet<>();

        for (int node : graph.keySet()) {
            if (!visited.contains(node)) {
                if (isCyclicUtil(graph, node, visited, recStack))
                    return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        graph.put(0, Arrays.asList(1));
        graph.put(1, Arrays.asList(2));
        graph.put(2, Arrays.asList(0));

        System.out.println("Graph contains cycle: " + isCyclic(graph));
    }
}
