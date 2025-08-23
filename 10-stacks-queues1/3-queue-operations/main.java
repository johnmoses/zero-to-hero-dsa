// Queue Operations - Java Example

import java.util.LinkedList;
import java.util.Queue;

public class QueueOperations {
    public static void main(String[] args) {
        Queue<Integer> queue = new LinkedList<>();

        queue.add(1);
        queue.add(2);

        if (!queue.isEmpty())
            System.out.println("Front element: " + queue.peek());

        if (!queue.isEmpty())
            System.out.println("Dequeue element: " + queue.poll());

        System.out.println("Is queue empty? " + queue.isEmpty());
    }
}
