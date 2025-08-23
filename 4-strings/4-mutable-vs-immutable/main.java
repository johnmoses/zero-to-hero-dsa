// Mutable vs Immutable Strings - Java Example

public class MutableVsImmutable {
    public static void main(String[] args) {
        String text = "hello";
        System.out.println("Original text: " + text);

        // String is immutable, so replace returns a new string
        String newText = text.replace('h', 'j');
        System.out.println("New text after replace: " + newText);
        System.out.println("Original text remains: " + text);

        // Using StringBuilder for mutable strings
        StringBuilder builder = new StringBuilder("hello");
        builder.setCharAt(0, 'j');
        System.out.println("Mutable StringBuilder text: " + builder.toString());
    }
}
