// String Searching - Java Example

class StringSearching {

    public static void main(String[] args) {
        String text = "Hello, world!";
        String substring = "world";

        int index = text.indexOf(substring);
        if (index != -1) {
            System.out.println("Index of 'world': " + index);
        } else {
            System.out.println("'world' not found");
        }
    }
}
