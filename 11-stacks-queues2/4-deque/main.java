// Deque - Java Example

import java.util.ArrayDeque;
import java.util.Deque;

public class DequeExample {

    public static void main(String[] args) {
        Deque<Integer> dq = new ArrayDeque<>();
        dq.addLast(1);   // add to right
        dq.addFirst(2);  // add to left

        System.out.println(dq);  // [2, 1]

        dq.removeLast();  // remove from right
        dq.removeFirst(); // remove from left

        System.out.println(dq);  // []
    }
}
