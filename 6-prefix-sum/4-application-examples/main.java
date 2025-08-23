// Application Examples - Java

public class ApplicationExamples {

    public static int countInRange(int[] prefix, int left, int right) {
        if (left == 0) {
            return prefix[right];
        }
        return prefix[right] - prefix[left - 1];
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 2, 3, 3, 3, 4};
        int maxVal = 0;
        for (int num : arr) {
            if (num > maxVal) maxVal = num;
        }

        int[] freq = new int[maxVal + 1];
        for (int num : arr) {
            freq[num]++;
        }

        int[] prefixFreq = new int[freq.length];
        prefixFreq[0] = freq;
        for (int i = 1; i < freq.length; i++) {
            prefixFreq[i] = prefixFreq[i - 1] + freq[i];
        }

        System.out.println("Count of numbers between 2 and 3: " + countInRange(prefixFreq, 2, 3));
    }
}
