/*
A Simple Algorithm:
    
Fibonacci numbers using native approach

Fibonacci numbers is a sequence such that
each number is the sum of the two preceeding ones starting from 0 and 1
So we have 0, 1, 1, 2, 3, 5, 8, 13, 21
*/

public class main {
    public static void main(String[] args) {
        int n = 10 ;
        int a = 0 ;
        int b = 1 ;
        System.out.print(a + " " + b + " ");
        for(int i = 2 ; i <= n ; i ++) {
            int c = a + b ;
            System.out.print(c + " ");
            a = b ;
            b = c ;
        }
    }
}