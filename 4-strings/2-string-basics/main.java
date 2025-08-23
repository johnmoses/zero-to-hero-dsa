// String Basics - Java Example

public class StringBasics {

    public static void main(String[] args) {
        String text = "hello";

        System.out.println("Length: " + text.length());
        System.out.println("First character: " + text.charAt(0));
        System.out.println("Uppercase: " + text.toUpperCase());
        System.out.println("Contains 'll': " + text.contains("ll"));
    }
}
