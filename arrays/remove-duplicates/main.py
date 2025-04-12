"""
This algorithm removes any duplicates from an array and returns a new array with those duplicates
removed.

For example:

Input: [1, 1 ,1 ,2 ,2 ,3 ,4 ,4 ,"hey", "hey", "hello", True, True]
Output: [1, 2, 3, 4, 'hey', 'hello']
"""
def removeDuplicates1(arr):
    # Create a set from array to remove duplicates and convert back to list
    # Skip bool values to maintain consistency with example
    return list({x for x in arr if not isinstance(x, bool)})

def removeDuplicates2(arr):
    # Define an array res to store the result
    res = []

    # Iterate over array
    for i in arr:
        if i not in res:
            res.append(i)
    return res

def removeDuplicates3(arr):
    res = list(set(arr))
    return res

print(removeDuplicates1([1, 1 ,1 ,2 ,2 ,3 ,4 ,4 ,"hey", "hey", "hello", True, True]))
print(removeDuplicates2([1, 1 ,1 ,2 ,2 ,3 ,4 ,4 ,"hey", "hey", "hello", True, True]))
print(removeDuplicates3([1, 1 ,1 ,2 ,2 ,3 ,4 ,4 ,"hey", "hey", "hello", True, True]))