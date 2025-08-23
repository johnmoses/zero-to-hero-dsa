// Array Operations - Java Example

import java.util.ArrayList;

public class ArrayOperations {

    public static void main(String[] args) {
        ArrayList<Integer> arr = new ArrayList<>();
        arr.add(1);
        arr.add(2);
        arr.add(3);
        arr.add(4);
        arr.add(5);

        // Traversal
        for (int element : arr) {
            System.out.println("Element: " + element);
        }

        // Insertion (append)
        arr.add(6);

        // Deletion (remove by value)
        arr.remove(Integer.valueOf(2));

        // Searching
        int index = arr.indexOf(4);
        System.out.println("Index of 4: " + index);

        // Updating
        arr.set(0, 10);

        System.out.print("Updated array: ");
        for (int e : arr) {
            System.out.print(e + " ");
        }
        System.out.println();
    }
}
