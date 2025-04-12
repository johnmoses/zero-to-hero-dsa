/**
 * Write a basic array queue data structure showing basic functionalities
 */
import java.util.ArrayList;
import java.util.List;

public class main {
    public static void main(String[] args) {
        System.out.println("Queues data structures");
        List<String> queue = new ArrayList<>();
        queue.add("A");
        queue.add("B");
        queue.add("C");
        System.out.println("Initial queue: " + queue);
        queue.remove(0);
        System.out.println("Queue after removing first element: " + queue);
    }
}