// Two Pointers Technique - Java Example

public class TwoPointersTechnique {

    public static int removeDuplicates(int[] arr) {
        if (arr.length == 0) return 0;
        int writeIndex = 1;
        for (int readIndex = 1; readIndex < arr.length; readIndex++) {
            if (arr[readIndex] != arr[readIndex - 1]) {
                arr[writeIndex] = arr[readIndex];
                writeIndex++;
            }
        }
        return writeIndex;
    }

    public static void main(String[] args) {
        int[] arr = {1,1,2,2,3,4,4};
        int newLength = removeDuplicates(arr);

        System.out.print("Array without duplicates: ");
        for (int i = 0; i < newLength; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }
}
