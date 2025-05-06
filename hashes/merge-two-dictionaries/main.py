""" 
Write code to merge two dictionaries.
"""
def merge_dicts1(dict1, dict2):
    # Update dict1 with dict2
    res = dict1.update(dict2)
    return res

# print(merge_dicts1({'a': 1, 'b': 2}, {'c': 3, 'd': 4}))

def merge_dicts2(dict1, dict2):
    # Use unpacking operator to unpack dict1 and dict2 into res
    res = {**dict1, **dict2}
    return res

print(merge_dicts2({'a': 1, 'b': 2}, {'c': 3, 'd': 4}))