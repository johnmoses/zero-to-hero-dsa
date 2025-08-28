// Strings - Java Example

class StringsIntro {

    public static void main(String[] args) {
        String text = "Hello, World!";
        System.out.println("Original string: " + text);

        // Concatenation
        String greeting = text + " Welcome!";
        System.out.println("Concatenated string: " + greeting);

        // Substring
        System.out.println("Substring (7,12): " + text.substring(7, 12));
    }
}
