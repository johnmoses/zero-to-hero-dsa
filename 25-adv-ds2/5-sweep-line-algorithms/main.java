// Sweep Line Algorithms - Java example (Counting overlapping intervals)

import java.util.*;

class Main {
    public static int countOverlaps(List<int[]> intervals) {
        List<int[]> events = new ArrayList<>();
        for (int[] interval : intervals) {
            events.add(new int[] {interval[0], 1});   // Interval start
            events.add(new int[] {interval[1], -1});  // Interval end
        }

        events.sort(Comparator.comparingInt(a -> a[0]));

        int active = 0, maxOverlaps = 0;

        for (int[] event : events) {
            active += event[1];
            maxOverlaps = Math.max(maxOverlaps, active);
        }

        return maxOverlaps;
    }

    public static void main(String[] args) {
        List<int[]> intervals = Arrays.asList(
            new int[]{1,3}, new int[]{2,5}, new int[]{4,6}, new int[]{7,8}
        );
        System.out.println(countOverlaps(intervals));  // Output: 3
    }
}
