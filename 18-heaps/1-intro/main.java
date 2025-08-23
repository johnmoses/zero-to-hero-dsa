// Heap Introduction - Java Example

import java.util.PriorityQueue;

public class HeapIntro {
    public static void main(String[] args) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        minHeap.add(5);
        minHeap.add(3);
        minHeap.add(8);

        System.out.println("Heap elements popped in order:");
        while (!minHeap.isEmpty()) {
            System.out.println(minHeap.poll());
        }
    }
}
