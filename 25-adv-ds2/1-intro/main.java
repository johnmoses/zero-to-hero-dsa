// Advanced Data Structures 2 - Intro Java example
// Bit manipulation: Counting set bits

class Main {
    public static int countSetBits(int n) {
        int count = 0;
        while (n != 0) {
            n &= (n - 1);
            count++;
        }
        return count;
    }

    public static void main(String[] args) {
        int num = 29; // Binary: 11101
        System.out.println(countSetBits(num));  // Output: 4
    }
}
