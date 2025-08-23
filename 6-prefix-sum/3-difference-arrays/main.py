# Difference Arrays - Python Example

def build_diff_array(arr):
    diff = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        diff[i] += arr[i]
        diff[i+1] -= arr[i] if i+1 < len(arr) else 0
    return diff

def update_range(diff, l, r, val):
    diff[l] += val
    if r + 1 < len(diff):
        diff[r+1] -= val

def reconstruct_array(diff):
    res = [0] * (len(diff) -1)
    curr = 0
    for i in range(len(res)):
        curr += diff[i]
        res[i] = curr
    return res

arr = [1, 2, 3, 4, 5]
diff = [0] * (len(arr) + 1)
for i, val in enumerate(arr):
    diff[i] += val
    diff[i+1] -= val

update_range(diff, 1, 3, 5)
result = reconstruct_array(diff[:-1])
print("Array after range update:", result)
