// Dijkstra's Algorithm - Java Example

import java.util.*;

class DijkstraAlgorithm {

    public static Map<Character, Integer> dijkstra(Map<Character, List<Pair>> graph, char start) {
        Map<Character, Integer> distances = new HashMap<>();
        for (Character vertex : graph.keySet()) {
            distances.put(vertex, Integer.MAX_VALUE);
        }
        distances.put(start, 0);

        PriorityQueue<Pair> pq = new PriorityQueue<>(Comparator.comparingInt(p -> p.weight));
        pq.add(new Pair(start, 0));

        while (!pq.isEmpty()) {
            Pair current = pq.poll();
            if (current.weight > distances.get(current.vertex)) continue;

            for (Pair neighbor : graph.getOrDefault(current.vertex, Collections.emptyList())) {
                int newDist = current.weight + neighbor.weight;
                if (newDist < distances.get(neighbor.vertex)) {
                    distances.put(neighbor.vertex, newDist);
                    pq.add(new Pair(neighbor.vertex, newDist));
                }
            }
        }
        return distances;
    }

    static class Pair {
        char vertex;
        int weight;
        Pair(char vertex, int weight) {
            this.vertex = vertex;
            this.weight = weight;
        }
    }

    public static void main(String[] args) {
        Map<Character, List<Pair>> graph = new HashMap<>();
        graph.put('A', Arrays.asList(new Pair('B',1), new Pair('C',4)));
        graph.put('B', Arrays.asList(new Pair('C',2), new Pair('D',5)));
        graph.put('C', Arrays.asList(new Pair('D',1)));
        graph.put('D', Collections.emptyList());

        Map<Character, Integer> distances = dijkstra(graph, 'A');
        System.out.println("Shortest distances from A: " + distances);
    }
}
