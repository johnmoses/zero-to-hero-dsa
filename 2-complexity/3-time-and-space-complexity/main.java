// Time and Space Complexity - Java Example

import java.util.ArrayList;
import java.util.List;

public class TimeSpaceComplexity {

    public static int sumList(List<Integer> items) {
        int total = 0; // O(1) space
        for (int item : items) { // O(n) time
            total += item;
        }
        return total;
    }

    public static List<Integer> copyList(List<Integer> items) {
        List<Integer> newList = new ArrayList<>(); // O(n) space
        for (int item : items) {                    // O(n) time
            newList.add(item);
        }
        return newList;
    }
}
