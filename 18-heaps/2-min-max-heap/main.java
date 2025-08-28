// Min and Max Heap - Java Example

import java.util.Collections;
import java.util.PriorityQueue;

class MinMaxHeapDemo {
    public static void main(String[] args) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

        int[] nums = {5, 3, 8, 1};
        for (int num : nums) {
            minHeap.add(num);
            maxHeap.add(num);
        }

        System.out.println("Min heap order:");
        while (!minHeap.isEmpty()) {
            System.out.println(minHeap.poll());
        }

        System.out.println("Max heap order:");
        while (!maxHeap.isEmpty()) {
            System.out.println(maxHeap.poll());
        }
    }
}
