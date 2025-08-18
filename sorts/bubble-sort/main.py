""" 
Bubble Sort

Example 1:
    Input: [64, 34, 25, 12, 22, 11, 90, 5]
    Output: [11, 12, 22, 25, 34, 5, 64, 90]
"""
def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

print(bubbleSort([64, 34, 25, 12, 22, 11, 90, 5]))
print(bubbleSort(['E','F','A','G','C','B','D']))
