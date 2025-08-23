// Dynamic Programming Intro - Java example
// Compute Fibonacci numbers using memoization

import java.util.HashMap;

public class Main {
    static HashMap<Integer, Integer> memo = new HashMap<>();
    
    public static int fib(int n) {
        if (memo.containsKey(n)) return memo.get(n);
        if (n <= 1) return n;
        int result = fib(n-1) + fib(n-2);
        memo.put(n, result);
        return result;
    }
    
    public static void main(String[] args) {
        int n = 10;
        System.out.println("Fibonacci number at position " + n + " is " + fib(n));
    }
}
