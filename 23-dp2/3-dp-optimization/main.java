// DP Optimization - Java example (Space Optimized Fibonacci)

public class Main {
    public static int fib(int n) {
        if (n <= 1) return n;
        int prev = 0, curr = 1;
        for (int i = 2; i <= n; i++) {
            int next = prev + curr;
            prev = curr;
            curr = next;
        }
        return curr;
    }

    public static void main(String[] args) {
        System.out.println(fib(10));  // Output: 55
    }
}
