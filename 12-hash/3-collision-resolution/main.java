// Collision Resolution - Java Example (Chaining)

import java.util.LinkedList;

class HashMap {
    private static class Entry {
        String key;
        int value;
        Entry(String key, int value) {
            this.key = key; this.value = value;
        }
    }

    private LinkedList<Entry>[] buckets;
    private int size;

    public HashMap(int size) {
        this.size = size;
        buckets = new LinkedList[size];
        for (int i = 0; i < size; i++)
            buckets[i] = new LinkedList<>();
    }

    private int hash(String key) {
        return Math.abs(key.hashCode()) % size;
    }

    public void insert(String key, int value) {
        int idx = hash(key);
        for (Entry e : buckets[idx]) {
            if (e.key.equals(key)) {
                e.value = value;
                return;
            }
        }
        buckets[idx].add(new Entry(key, value));
    }

    public Integer get(String key) {
        int idx = hash(key);
        for (Entry e : buckets[idx]) {
            if (e.key.equals(key))
                return e.value;
        }
        return null;
    }
}

class CollisionResolution {
    public static void main(String[] args) {
        HashMap hmap = new HashMap(10);
        hmap.insert("apple", 3);
        hmap.insert("banana", 5);
        System.out.println("Apple count: " + hmap.get("apple"));
    }
}
