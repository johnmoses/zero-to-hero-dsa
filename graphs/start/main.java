/**
 Graph Representation

 Given the nodes ['A', 'B', 'C', 'D', 'E'] and 
 edges edges = [
    [0, 1, 1, 1, 0],  # Edges for A
    [1, 0, 1, 0, 0],  # Edges for B
    [1, 1, 0, 0, 0],  # Edges for C
    [1, 0, 0, 0, 0],  # Edges for D
    [0, 1, 0, 0, 1]   # Edges for E
], Write a basic adjacency matrix graph representation in Java.
 */

public class main {
    private int V;
    private int[][] adjMatrix;
    private char[] vertices;

    public main(int vertices) {
        this.V = vertices;
        adjMatrix = new int[V][V];
        this.vertices = new char[V];
    }


    public void addVertex(int index, char label) {
        vertices[index] = label;
    }


    public void addEdge(int i, int j) {
        adjMatrix[i][j] = 1;
    }


    public static main createSampleGraph() {
        main g = new main(5);
        char[] nodes = {'A', 'B', 'C', 'D', 'E'};
        
        // Add vertices
        for(int i = 0; i < nodes.length; i++) {
            g.addVertex(i, nodes[i]);
        }


        // Add edges from adjacency matrix
        int[][] edges = {
            {0, 1, 1, 1, 0},
            {1, 0, 1, 0, 0},
            {1, 1, 0, 0, 0},
            {1, 0, 0, 0, 0},
            {0, 1, 0, 0, 1}
        };

        for(int i = 0; i < edges.length; i++) {
            for(int j = 0; j < edges[i].length; j++) {

                if(edges[i][j] == 1) {
                    g.addEdge(i, j);
                }
            }
        }
        return g;
    }

    public void printGraph() {
        System.out.print("  ");
        for(char v : vertices) {
            System.out.print(v + " ");
        }
        System.out.println();

        for(int i = 0; i < V; i++) {
            System.out.print(vertices[i] + " ");
            for(int j = 0; j < V; j++) {
                System.out.print(adjMatrix[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        main g = createSampleGraph();
        g.printGraph();
    }
}
