// Stack and Queue Introduction - Java Example

import java.util.Stack;
import java.util.LinkedList;
import java.util.Queue;

public class StacksQueuesIntro {
    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<>();
        stack.push(1);
        stack.push(2);
        System.out.println("Stack pop: " + stack.pop());

        Queue<Integer> queue = new LinkedList<>();
        queue.add(1);
        queue.add(2);
        System.out.println("Queue pop: " + queue.poll());
    }
}
