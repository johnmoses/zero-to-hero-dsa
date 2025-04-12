"""
Index of minimum item
"""

def index_of_min(data):
    min_index = 0
    current_index = 1
    while current_index < len(data):
        if data[current_index] < data[min_index]:
            min_index = current_index
        current_index += 1
    return min_index

data = [1,2,3]
print('Minimum index...', index_of_min(data))