// Stack Operations - Java Example

import java.util.Stack;

public class StackOperations {
    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<>();

        stack.push(1);
        stack.push(2);

        if (!stack.isEmpty())
            System.out.println("Top element: " + stack.peek());

        if (!stack.isEmpty())
            System.out.println("Pop element: " + stack.pop());

        System.out.println("Is stack empty? " + stack.isEmpty());
    }
}
