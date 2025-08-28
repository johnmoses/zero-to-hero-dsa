// main.java
// Java example code demonstrating basic programming concepts.

class HelloWorld {
    
    // Method to print Hello World
    public static void helloWorld() {
        System.out.println("Hello, World!");
    }

    // Method to add two numbers
    public static int addNumbers(int a, int b) {
        return a + b;
    }

    // Recursive method to calculate factorial
    public static int factorial(int n) {
        if (n == 0) {
            return 1;
        } else {
            return n * factorial(n - 1);
        }
    }

    public static void main(String[] args) {
        helloWorld();
        System.out.println("Sum of 3 and 5: " + addNumbers(3, 5));
        System.out.println("Factorial of 5: " + factorial(5));
    }
}
