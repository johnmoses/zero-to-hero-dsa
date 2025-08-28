// Memoization - Java example

import java.util.HashMap;

class Main {
    static HashMap<Integer, Integer> memo = new HashMap<>();
    
    public static int fib(int n) {
        if (memo.containsKey(n)) return memo.get(n);
        if (n <= 1) return n;
        int result = fib(n-1) + fib(n-2);
        memo.put(n, result);
        return result;
    }
    
    public static void main(String[] args) {
        System.out.println(fib(10));  // Output: 55
    }
}
