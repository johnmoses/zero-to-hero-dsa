// Hashing - Java Example

import java.util.HashMap;

class HashingIntro {

    public static void main(String[] args) {
        HashMap<String, Integer> hashMap = new HashMap<>();

        // Insert
        hashMap.put("apple", 3);
        hashMap.put("banana", 5);

        // Lookup
        System.out.println("Apple count: " + hashMap.getOrDefault("apple", 0));

        // Update
        hashMap.put("apple", hashMap.get("apple") + 2);
        System.out.println("Updated apple count: " + hashMap.get("apple"));
    }
}
