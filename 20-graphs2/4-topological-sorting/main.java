// Topological Sorting - Java Example (DFS based)

import java.util.*;

class TopologicalSort {

    private static void topologicalSortUtil(int v, List<List<Integer>> adj, boolean[] visited, Stack<Integer> stack) {
        visited[v] = true;
        for (int neighbor : adj.get(v)) {
            if (!visited[neighbor])
                topologicalSortUtil(neighbor, adj, visited, stack);
        }
        stack.push(v);
    }

    private static List<Integer> topologicalSort(int V, List<int[]> edges) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < V; i++) {
            adj.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            adj.get(edge[0]).add(edge[10]);
        }

        boolean[] visited = new boolean[V];
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < V; i++) {
            if (!visited[i]) {
                topologicalSortUtil(i, adj, visited, stack);
            }
        }

        List<Integer> result = new ArrayList<>();
        while (!stack.isEmpty()) {
            result.add(stack.pop());
        }
        return result;
    }

    public static void main(String[] args) {
        int V = 6;
        List<int[]> edges = Arrays.asList(
            new int[]{2, 3},
            new int[]{3, 1},
            new int[]{4, 0},
            new int[]{4, 1},
            new int[]{5, 0},
            new int[]{5, 2}
        );

        List<Integer> result = topologicalSort(V, edges);
        System.out.println("Topological sort order: " + result);
    }
}
