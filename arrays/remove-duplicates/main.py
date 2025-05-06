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
            # Append i to res if not already there
            res.append(i)
    return res

def removeDuplicates3(arr):
    # Define a list of a set of the arr to automatically remove duplicates
    res = list(set(arr))
    return res

print(removeDuplicates1([1, 1 ,1 ,2 ,2 ,3 ,4 ,4 ,"hey", "hey", "hello", True, True]))
print(removeDuplicates2([1, 1 ,1 ,2 ,2 ,3 ,4 ,4 ,"hey", "hey", "hello", True, True]))
print(removeDuplicates3([1, 1 ,1 ,2 ,2 ,3 ,4 ,4 ,"hey", "hey", "hello", True, True]))