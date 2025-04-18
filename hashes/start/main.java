/**
 * Hashes

Design a hash map with ability to insert, access and delete items.

Example 1:
    Input
    ["HashMap", "insert", "insert", "get", "get", "insert", "get", "delete", "get"]
    [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
    Output
    [null, null, null, 1, -1, null, 1, null, -1]

Constraints:
0 <= key, value <= 106
At most 104 calls will be made to put, get, and remove.
 */
class HashMap {
    private static final int SIZE = 10007;
    private Entry[] table;

    private static class Entry {
        int key, value;
        Entry next;
        Entry(int key, int value) {
            this.key = key;
            this.value = value;
        }

    }

    public HashMap() {
        table = new Entry[SIZE];
    }


    private int hash(int key) {
        return key % SIZE;
    }


    public void insert(int key, int value) {
        int index = hash(key);
        Entry current = table[index];
        
        while (current != null) {
            if (current.key == key) {
                current.value = value;
                return;
            }
            current = current.next;
        }


        Entry newEntry = new Entry(key, value);
        newEntry.next = table[index];
        table[index] = newEntry;
    }


    public int get(int key) {
        int index = hash(key);
        Entry current = table[index];
        
        while (current != null) {
            if (current.key == key) {
                return current.value;
            }
            current = current.next;
        }
        return -1;
    }


    public void delete(int key) {
        int index = hash(key);
        Entry current = table[index];
        Entry prev = null;
        
        while (current != null) {
            if (current.key == key) {
                if (prev == null) {
                    table[index] = current.next;
                } else {
                    prev.next = current.next;
                }
                return;
            }
            prev = current;
            current = current.next;
        }
    }

    public void print() {
        for (int i = 0; i < SIZE; i++) {
            Entry current = table[i];
            while (current != null) {
                System.out.println("Key: " + current.key + ", Value: " + current.value);
                current = current.next;
            }
        }
    }

    public static void main(String[] args) {
        HashMap hashMap = new HashMap();
        hashMap.insert(1, 1);
        hashMap.insert(2, 2);
        System.out.println(hashMap.get(1)); // Output: 1
        System.out.println(hashMap.get(3)); // Output: -1
        hashMap.insert(2, 1);
        System.out.println(hashMap.get(2)); // Output: 1
        hashMap.delete(2);
        System.out.println(hashMap.get(2)); // Output: -1
        hashMap.insert(3, 3);
        System.out.println(hashMap.get(3)); // Output: 3
        hashMap.print();
    }
}

/**
 * Design a hash set with insert, contains and delete behaviours.

Example 1:
    ["HashSet", "insert", "insert", "contains", "contains", "insert", "contains", "delete", "contains"]
    [[], [1], [2], [1], [3], [2], [2], [2], [2]]
    Output
    [null, null, null, true, false, nul

Constraints:
0 <= key <= 106
At most 104 calls will be made to insert, delete, and contains.
 */
class HashSet {
    private static final int SIZE = 10007;
    private Entry[] table;

    private static class Entry {
        int key;
        Entry next;
        Entry(int key) {
            this.key = key;
        }
    }

    public HashSet() {
        table = new Entry[SIZE];
    }

    private int hash(int key) {
        return key % SIZE;
    }

    public void insert(int key) {
        int index = hash(key);
        Entry current = table[index];

        while (current != null) {
            if (current.key == key) {
                return;
            }
            current = current.next;
        }

        Entry newEntry = new Entry(key);
        newEntry.next = table[index];
        table[index] = newEntry;
    }

    public boolean contains(int key) {
        int index = hash(key);
        Entry current = table[index];

        while (current != null) {
            if (current.key == key) {
                return true;
            }
            current = current.next;
        }
        return false;
    }

    public void delete(int key) {
        int index = hash(key);
        Entry current = table[index];
        Entry prev = null;

        while (current != null) {
            if (current.key == key) {
                if (prev == null) {
                    table[index] = current.next;
                } else {
                    prev.next = current.next;
                }
                return;
            }
            prev = current;
            current = current.next;
        }
    }

    public void print() {
        for (int i = 0; i < SIZE; i++) {
            Entry current = table[i];
            while (current != null) {
                System.out.println("Key: " + current.key);
                current = current.next;
            }
        }
    }

    public static void main(String[] args) {
        HashSet hashSet = new HashSet();
        hashSet.insert(1);
        hashSet.insert(2);
        System.out.println(hashSet.contains(1)); // Output: true
        System.out.println(hashSet.contains(3)); // Output: false
        hashSet.insert(2);
        System.out.println(hashSet.contains(2)); // Output: true
        hashSet.delete(2);
        System.out.println(hashSet.contains(2)); // Output: false
        hashSet.insert(3);
        System.out.println(hashSet.contains(3)); // Output: true
        hashSet.print();
    }
}