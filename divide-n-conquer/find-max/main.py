""" 
Find maximum element in the list
Input: [1,2,6,4,3,5,8,14,7]
Output: 14
"""

def find_max(data):
    #return
    biggest = data[0]
    for val in data:
        if val > biggest:
            biggest = val
    return biggest

print(find_max([1,2,6,4,3,5,8,14,7]))