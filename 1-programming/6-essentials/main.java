// main.java
// Java examples demonstrating programming essentials like comments, input/output, and error handling.

import java.util.Scanner;

class Main {
    // Function to greet user by name
    public static void greet(String name) {
        System.out.println("Hello, " + name);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter your name: ");
        String name = scanner.nextLine();

        if (name.isEmpty()) {
            System.err.println("Error: Name cannot be empty!");
            System.exit(1);
        }

        greet(name);
        scanner.close();
    }
}
