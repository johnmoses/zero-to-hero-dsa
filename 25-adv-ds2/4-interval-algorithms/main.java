// Interval Algorithms - Java example (Merge Intervals)

import java.util.*;

public class Main {
    public static List<int[]> mergeIntervals(List<int[]> intervals) {
        if (intervals.isEmpty()) return Collections.emptyList();

        intervals.sort(Comparator.comparingInt(a -> a[0]));
        List<int[]> merged = new ArrayList<>();
        merged.add(intervals.get(0));

        for (int i = 1; i < intervals.size(); i++) {
            int[] last = merged.get(merged.size() - 1);
            int[] current = intervals.get(i);

            if (current[0] <= last) {
                last = Math.max(last, current);
            } else {
                merged.add(current);
            }
        }
        return merged;
    }

    public static void main(String[] args) {
        List<int[]> intervals = new ArrayList<>();
        intervals.add(new int[] {1, 3});
        intervals.add(new int[] {2, 6});
        intervals.add(new int[] {8, 10});
        intervals.add(new int[] {15, 18});

        List<int[]> merged = mergeIntervals(intervals);
        for (int[] interval : merged) {
            System.out.print("(" + interval[0] + ", " + interval + ") ");
        }
        // Output: (1, 6) (8, 10) (15, 18)
    }
}
