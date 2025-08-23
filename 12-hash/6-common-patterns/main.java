// Common Hashing Problems - Java Example

import java.util.HashMap;
import java.util.HashSet;
import java.util.ArrayList;
import java.util.List;

public class CommonHashProblems {

    // Anagram check
    public static boolean areAnagrams(String s1, String s2) {
        if (s1.length() != s2.length()) return false;
        int[] freq = new int[256];  // Assuming ASCII
        for (char c : s1.toCharArray()) freq[c]++;
        for (char c : s2.toCharArray()) {
            freq[c]--;
            if (freq[c] < 0) return false;
        }
        return true;
    }

    // Intersection of arrays
    public static List<Integer> arrayIntersection(int[] arr1, int[] arr2) {
        HashSet<Integer> set1 = new HashSet<>();
        for (int num : arr1) set1.add(num);
        List<Integer> result = new ArrayList<>();
        for (int num : arr2) {
            if (set1.contains(num)) {
                result.add(num);
            }
        }
        return result;
    }

    // Two sum
    public static int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hashMap = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (hashMap.containsKey(complement)) {
                return new int[]{hashMap.get(complement), i};
            }
            hashMap.put(nums[i], i);
        }
        return new int[]{-1, -1};
    }

    public static void main(String[] args) {
        System.out.println("Are 'listen' and 'silent' anagrams? " + areAnagrams("listen", "silent"));

        List<Integer> intersection = arrayIntersection(new int[]{1,2,2,1}, new int[]{2,2});
        System.out.print("Intersection: ");
        for (int x : intersection) {
            System.out.print(x + " ");
        }
        System.out.println();

        int[] indices = twoSum(new int[]{2,7,11,15}, 9);
        System.out.println("Two sum indices: (" + indices[0] + ", " + indices + ")");
    }
}
