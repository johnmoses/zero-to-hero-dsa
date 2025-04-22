/**
 * Hashes
 * Create a basic hash table to store adn access fruits based on their first letters.
 */
public class main {
    public static void main(String[] args) {
        String[] fruits = {"apple", "banana", "cherry"};

        // Create a hash table with 3 buckets
        String[] hashTable = new String[3];

        // Hash each fruit into the hash table
        for (String fruit : fruits) {
            int index = fruit.charAt(0) - 'a';
            hashTable[index] = fruit;
        }

        // Access fruits based on their first letter
        char[] letters = {'a', 'b', 'c'};

        for (char letter : letters) {
            int index = letter - 'a';
            String fruit = hashTable[index];
            if (fruit != null) {
                System.out.println("Fruit starting with '" + letter + "': " + fruit);
            }
        }
    }
}
