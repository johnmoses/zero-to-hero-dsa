/**
 * Simple Sort Algorithm

Write a basic sort algorithm that takes a list of numbers and returns a sorted list.

Example 1:
    Input: [1, 5, 2, 3, 4]
    Output: [1, 2, 3, 4, 5]

Example 2:
    Input: [5, 4, 3, 2, 1]
    Output: [1, 2, 3, 4, 5]
 */
/**
 * Sorts a list of numbers in ascending order using bubble sort
 * @param numbers Input array of integers
 * @return Sorted array in ascending order
 */
public class main {
    public static int[] sort(int[] numbers) {
        int temp;
        for (int i = 0; i < numbers.length; i++) {
            for (int j = 1; j < numbers.length - i; j++) {
                if (numbers[j - 1] > numbers[j]) {
                    temp = numbers[j - 1];
                    numbers[j - 1] = numbers[j];
                    numbers[j] = temp;
                }
            }
        }
        return numbers;
    }
    public static void main(String[] args) {
        int[] numbers = {1, 5, 2, 3, 4};
        int[] sorted = sort(numbers);
        for (int i = 0; i < sorted.length; i++) {
            System.out.println(sorted[i]);
        }
    }
}