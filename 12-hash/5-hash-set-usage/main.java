// Hash Function - Java Example

public class HashFunction {

    public static int simpleHash(int key, int size) {
        return key % size;
    }

    public static void main(String[] args) {
        int size = 10;
        int[] keys = {15, 25, 35};
        for (int key : keys) {
            System.out.println("Hashed key for " + key + ": " + simpleHash(key, size));
        }
    }
}
