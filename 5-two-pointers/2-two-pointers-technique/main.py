# Two Pointers Technique - Python Example

def remove_duplicates(arr):
    if not arr:
        return 0
    write_index = 1
    for read_index in range(1, len(arr)):
        if arr[read_index] != arr[read_index - 1]:
            arr[write_index] = arr[read_index]
            write_index += 1
    return write_index  # New length of array without duplicates

arr = [1,1,2,2,3,4,4]
new_length = remove_duplicates(arr)
print("Array without duplicates:", arr[:new_length])
