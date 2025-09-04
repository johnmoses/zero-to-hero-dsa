// Common problems with strings in Java
class CommonStringProblems {
    public static void main(String[] args) {
        // Problem 1: Uninitialized string
        String uninitialized; // Declaration without initialization
        // System.out.println("Uninitialized string: " + uninitialized); // Compile-time error  
        // Correct way: Initialize the string
        uninitialized = "";
        System.out.println("Uninitialized string (should be empty): '" + uninitialized + "'");  // Output: Uninitialized string (should be empty): ''  
    }
}