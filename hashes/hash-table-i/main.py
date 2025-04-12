""" 
Hash Table
"""
BUCKET_SIZE = 7
arr = [15, 11, 27, 8, 12]

class HashTable(object):
    def __init__(self, bucket):
        # Number of buckets
        self.__bucket = bucket
        # Hash table of size bucket
        self.__table = [[] for _ in range(bucket)]

    # hash function to map values to key
    def hashFunction(self, key):
        return (key % self.__bucket)

    def insertItem(self, key):
        # get the hash index of key
        index = self.hashFunction(key)
        self.__table[index].append(key)

    def deleteItem(self, key):
        # get the hash index of key
        index = self.hashFunction(key)

        # Check the key in the hash table
        if key not in self.__table[index]:
            return

        # delete the key from hash table
        self.__table[index].remove(key)

    # function to display hash table
    def displayHash(self):
        for i in range(self.__bucket):
            print("[%d]" % i, end='')
            for x in self.__table[i]:
                print(" --> %d" % x, end='')
            print()

# Create a empty has of BUCKET_SIZE
h = HashTable(BUCKET_SIZE)

# insert the keys into the hash table
for x in arr:
    h.insertItem(x)

# delete 12 from the hash table
h.deleteItem(x)
# Display the hash table
h.displayHash()
