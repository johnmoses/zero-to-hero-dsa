"""
Hash Sets, hash function
"""
hash_set = [None,'Joy',None,'Lisa',None,'Bob',None,'Mary','Pete',None]

def hash_function(value):
    sum_of_chars = 0
    for char in value:
        sum_of_chars += ord(char)

    return sum_of_chars % 10
    
def contains(name):
    index = hash_function(name)
    return hash_set[index] == name

item = 'Bob'
print(f"Hash set contains {item}",contains(item))