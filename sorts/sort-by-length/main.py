""" 
Suppose you were given a list of strings [“hello”, everyone, “we”, “are”, “learning, “sorting”],
what is the most efficient way of sorting it?
"""
def sort_strings(strings):
    return sorted(strings, key=lambda x: (len(x), x))

print(sort_strings(["hello", "everyone", "we", "are", "learning", "sorting"]))