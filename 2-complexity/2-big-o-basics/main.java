// Big O Basics - Java Example

class BigOBasics {

    public static int constantTime(int[] items) {
        return items[0];  // O(1)
    }

    public static int logarithmicTime(int n) {
        int count = 0;
        while (n > 1) {
            n /= 2;
            count++;
        }
        return count;  // O(log n)
    }

    public static int quadraticTime(int[] items) {
        int count = 0;
        for (int i = 0; i < items.length; i++) {
            for (int j = 0; j < items.length; j++) {
                count++;
            }
        }
        return count;  // O(n^2)
    }

    public static void main(String[] args) {
        int[] data = {1, 2, 3};
        System.out.println("Constant time result: " + constantTime(data));
        System.out.println("Logarithmic steps: " + logarithmicTime(16));
        System.out.println("Quadratic operations: " + quadraticTime(data));
    }
}
