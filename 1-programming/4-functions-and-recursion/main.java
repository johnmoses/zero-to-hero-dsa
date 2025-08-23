// 4 Functions And Recursion - Java example

public class Main {
    public static void greet(String name) {
        System.out.println("Hello, " + name);
    }

    public static int factorial(int n) {
        if (n == 0)
            return 1;
        else
            return n * factorial(n - 1);
    }

    public static void main(String[] args) {
        greet("Alice");
        System.out.println("Factorial of 5: " + factorial(5));
    }
}
