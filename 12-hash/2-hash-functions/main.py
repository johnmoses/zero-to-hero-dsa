# Hash Function - Python Example

def simple_hash(key, size):
    return key % size

size = 10
keys = [15, 25, 35]
hashed = [simple_hash(k, size) for k in keys]

print("Hashed keys:", hashed)
