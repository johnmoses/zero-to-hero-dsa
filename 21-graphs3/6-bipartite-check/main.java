// Bipartite Graph Check using BFS - Java Example

import java.util.*;

public class BipartiteCheck {

    public static boolean isBipartite(List<List<Integer>> graph) {
        int n = graph.size();
        int[] color = new int[n];
        Arrays.fill(color, -1);

        for (int i = 0; i < n; i++) {
            if (color[i] == -1) {
                Queue<Integer> queue = new LinkedList<>();
                queue.offer(i);
                color[i] = 0;

                while (!queue.isEmpty()) {
                    int u = queue.poll();
                    for (int v : graph.get(u)) {
                        if (color[v] == -1) {
                            color[v] = 1 - color[u];
                            queue.offer(v);
                        } else if (color[v] == color[u]) {
                            return false;
                        }
                    }
                }
            }
        }
        return true;
    }

    public static void main(String[] args) {
        List<List<Integer>> graph1 = Arrays.asList(
            Arrays.asList(1, 3),
            Arrays.asList(0, 2),
            Arrays.asList(1, 3),
            Arrays.asList(0, 2)
        );

        List<List<Integer>> graph2 = Arrays.asList(
            Arrays.asList(1, 2),
            Arrays.asList(0, 2),
            Arrays.asList(0, 1)
        );

        System.out.println("Graph1 is bipartite: " + isBipartite(graph1));
        System.out.println("Graph2 is bipartite: " + isBipartite(graph2));
    }
}
