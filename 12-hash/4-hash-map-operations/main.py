# Hashing - Python Example

hash_map = {}

# Insert
hash_map["apple"] = 3
hash_map["banana"] = 5

# Lookup
print("Apple count:", hash_map.get("apple", 0))

# Update
hash_map["apple"] += 2
print("Updated apple count:", hash_map["apple"])
