// Prim's Algorithm for MST - Java Example

import java.util.*;

public class PrimMST {

    static class Edge {
        int to, weight;
        Edge(int to, int weight) {
            this.to = to;
            this.weight = weight;
        }
    }

    public static List<int[]> primMST(List<List<Edge>> graph) {
        int V = graph.size();
        boolean[] inMST = new boolean[V];
        PriorityQueue<Edge> pq = new PriorityQueue<>(Comparator.comparingInt(e -> e.weight));
        List<int[]> mstEdges = new ArrayList<>();
        int totalWeight = 0;

        pq.add(new Edge(0, 0));
        int[] parent = new int[V];
        Arrays.fill(parent, -1);

        while (!pq.isEmpty()) {
            Edge edge = pq.poll();
            int vertex = edge.to;

            if (inMST[vertex]) continue;

            inMST[vertex] = true;
            totalWeight += edge.weight;

            if (parent[vertex] != -1) {
                mstEdges.add(new int[]{parent[vertex], vertex});
            }

            for (Edge adjEdge : graph.get(vertex)) {
                if (!inMST[adjEdge.to]) {
                    pq.add(adjEdge);
                    parent[adjEdge.to] = vertex;
                }
            }
        }

        System.out.println("Total weight of MST: " + totalWeight);
        return mstEdges;
    }

    public static void main(String[] args) {
        List<List<Edge>> graph = Arrays.asList(
            Arrays.asList(new Edge(1, 2), new Edge(3, 6)),
            Arrays.asList(new Edge(0, 2), new Edge(2, 3), new Edge(3, 8), new Edge(4, 5)),
            Arrays.asList(new Edge(1, 3), new Edge(4, 7)),
            Arrays.asList(new Edge(0, 6), new Edge(1, 8)),
            Arrays.asList(new Edge(1, 5), new Edge(2, 7))
        );

        List<int[]> mstEdges = primMST(graph);
        System.out.println("Edges in MST:");
        for (int[] edge : mstEdges) {
            System.out.println(edge[0] + " - " + edge);
        }
    }
}
