// main.java
// Java examples demonstrating control flow statements.

class CheckNumber {

    public static void checkNumber(int num) {
        if (num > 0) {
            System.out.println(num + " is Positive");
        } else if (num == 0) {
            System.out.println(num + " is Zero");
        } else {
            System.out.println(num + " is Negative");
        }
    }

    public static void main(String[] args) {
        for (int i = -1; i <= 1; i++) {
            checkNumber(i);
        }
    }
}
