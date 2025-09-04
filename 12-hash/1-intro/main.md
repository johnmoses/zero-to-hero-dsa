# Introduction to Hashing

## Introduction
Hashing is a technique that maps data to fixed-size values (hash codes), enabling efficient data retrieval.

Python's `dict` class has an abstraction called `dictionary` in which unique keys are mapped to associated values. This is why a dictionaries are sometimes called associative arrays or maps. For example, we can map letters of the alphabets to numbers. There are five basic behaviours to start with, `__getitem__`, `__setitem__`, `__len__`, `__iter__` and  `__delitem__`.

Maps extends a dictionary, an abstraction where unique keys are mapped to associative values. A real-world example os this is storing country name and associating it with their currencies.Maps could be sorted or unsorted

## Details
Hash functions convert keys into indices in hash tables, supporting near O(1) average time complexity for insertions, deletions, and lookups.

Good hashing minimizes collisions, which occur when multiple keys map to the same index.

## Hash Tables

A hash table is a list of paired values. It is a practical implementation of a map data structure.
It organizes data using hash functions in order to support quick insertion, removal, search, look-up. Basic types include the hash set and the hash mal

## The Principle of Hash Table

The key idea of Hash Table is to use a hash function to map keys to buckets. To be more specific,

1. When we insert a new key, the hash function will decide which bucket the key should be assigned and the key will be stored in the corresponding bucket;
2. When we want to search for a key, the hash table will use the same hash function to find the corresponding bucket and search only in the specific bucket.

## Keys to hash table design

There are two basic keys to the design of hash tables

- Hash Functions
- Collision Resolution

## Hash Sets

The hash set is one of the implementations of a set data structure to store no repeated values.
The hash map is one of the implementations of a map data structure to store (key, value) pairs.

## Sets

Another implementation of maps. Set operations including add, remove, and lookup are highly efficient, in a constant time O(1)

A set is an unordered collection of elements, without duplicates, that typically supports efficient membership tests. Unlike maps, elements in a set do not have auxilary values, they are jusk keys.

## Examples
Storing user credentials in a hash map for fast access.

## Key Concepts
- Hash functions convert keys to indices.  
- Collision handling essential for correctness.  
- Hash tables provide fast average lookup.

## Summary
Hashing is fundamental for efficient data storage and retrieval across computer science.
