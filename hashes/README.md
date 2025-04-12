# Hashes

Hashing is the process of mapping any amount of data to a specified size using an algorithm. Related to this is encryption, a two-way process.

Common hashing algorithms includes MDS, SHA, SHA256 and Luhn

## Hash Tables

A hash table is a list of paired values. It is a practical implementation of a map data structure.
It organizes data using hash functions in order to support quick insertion, removal, search, look-up.

Types of Hash Tables

- Hash Set
- Hash Map

Maps extends a dictionary, an abstraction where unique keys are mapped to associative values. A real-world example os this is storing country name and associating it with their currencies.Maps could be sorted or unsorted

The hash set is one of the implementations of a set data structure to store no repeated values.
The hash map is one of the implementations of a map data structure to store (key, value) pairs.

## The Principle of Hash Table

The key idea of Hash Table is to use a hash function to map keys to buckets. To be more specific,

1. When we insert a new key, the hash function will decide which bucket the key should be assigned and the key will be stored in the corresponding bucket;
2. When we want to search for a key, the hash table will use the same hash function to find the corresponding bucket and search only in the specific bucket.

## Keys to hash table design

There are two basic keys to the design of hash tables

### Hash Functions

### Collision Resolution

## Skip List

This is another implementation of maps

## Sets

Another implementation of maps. Set operations including add, remove, and lookup are highly efficient, in a constant time O(1)
