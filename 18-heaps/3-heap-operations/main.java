// Heap Operations - Java Example

import java.util.ArrayList;

public class HeapOperations {

    public static void heapify(ArrayList<Integer> arr, int n, int i) {
        int largest = i;
        int left = 2*i + 1;
        int right = 2*i + 2;

        if (left < n && arr.get(left) > arr.get(largest))
            largest = left;

        if (right < n && arr.get(right) > arr.get(largest))
            largest = right;

        if (largest != i) {
            int temp = arr.get(i);
            arr.set(i, arr.get(largest));
            arr.set(largest, temp);

            heapify(arr, n, largest);
        }
    }

    public static void insert(ArrayList<Integer> heap, int val) {
        heap.add(val);
        int current = heap.size() - 1;
        while(current > 0) {
            int parent = (current - 1) / 2;
            if (heap.get(current) > heap.get(parent)) {
                int temp = heap.get(current);
                heap.set(current, heap.get(parent));
                heap.set(parent, temp);
                current = parent;
            } else {
                break;
            }
        }
    }

    public static int extractMax(ArrayList<Integer> heap) {
        if (heap.size() == 0) return -1;
        int maxVal = heap.get(0);
        int last = heap.remove(heap.size() - 1);
        if (!heap.isEmpty()) {
            heap.set(0, last);
            heapify(heap, heap.size(), 0);
        }
        return maxVal;
    }

    public static void main(String[] args) {
        ArrayList<Integer> heap = new ArrayList<>();
        insert(heap, 3);
        insert(heap, 4);
        insert(heap, 9);
        insert(heap, 5);
        insert(heap, 2);

        System.out.println("Max heap array: " + heap);
        System.out.println("Extract max: " + extractMax(heap));
        System.out.println("Heap after extraction: " + heap);
    }
}
