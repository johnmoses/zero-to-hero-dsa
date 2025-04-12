/**
import java.util.ArrayList;
 Suppose you were given a list of strings [“hello”, everyone, “we”, “are”, “learning, “sorting”],
what is the most efficient way of sorting it?
 */
import java.util.Arrays;
import java.util.Comparator;


public class main {
    public void sortByLength(String[] arr) {
        // Sorts a list of string by length of each string
        Arrays.sort(arr, new StringCompare());
    }
    public static void main(String[] args) {
        String[] arr = {"hello", "everyone", "we", "are", "learning", "sorting"};
        main m = new main();
        m.sortByLength(arr);
        for (String s : arr) {
            System.out.println(s);
        }
    }
}

class StringCompare implements Comparator<String> {
    public int compare(String s1, String s2) {
        if (s1.length() > s2.length()) {
            return 1;
        } else if (s1.length() < s2.length()) {
            return -1;
        }
        return 0;
    }
}