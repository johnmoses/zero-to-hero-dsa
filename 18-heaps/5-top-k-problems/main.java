// Top K Elements - Java Example

import java.util.PriorityQueue;

class TopKElements {

    public static int[] findTopKElements(int[] arr, int k) {
        if (k <= 0) return new int[0];
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        for (int num : arr) {
            if (minHeap.size() < k) {
                minHeap.add(num);
            } else if (num > minHeap.peek()) {
                minHeap.poll();
                minHeap.add(num);
            }
        }
        int[] result = new int[minHeap.size()];
        int i = 0;
        for (int val : minHeap)
            result[i++] = val;
        return result;
    }

    public static void main(String[] args) {
        int[] arr = {3, 1, 4, 1, 5, 9, 2, 6, 5};
        int k = 3;
        int[] topK = findTopKElements(arr, k);
        System.out.print("Top " + k + " elements are: ");
        for (int val : topK)
            System.out.print(val + " ");
    }
}
