/**
 * Recursion

Write a simple recursion algorithm
to print numbers from 1 to n in normal order and then print numbers from n to 1 in reverse order.
 */
public class main {
    
    public static void printNumbers(int n) {
        if (n <= 0) {
            return;
        }
        // Print ascending numbers first
        printAscending(1, n);
        // Print descending numbers
        printDescending(n);
    }


    private static void printAscending(int current, int n) {
        if (current > n) {
            return;
        }
        System.out.print(current + " ");
        printAscending(current + 1, n);
    }


    private static void printDescending(int n) {
        if (n <= 0) {
            return;
        }
        System.out.print(n + " ");
        printDescending(n - 1);
    }

    public static void main(String[] args) {
        int n = 5;
        printNumbers(n);
    }

}