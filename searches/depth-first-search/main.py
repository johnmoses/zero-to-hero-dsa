"""
Depth First Search
"""

def depth_first_search(data, start, visited=set()):
    # if not visited print it
    if start not in visited:
        print(start, end=" ")

    visited.add(start)

    for i in data[start] - visited:
        # if not visited gi in dept of it
        depth_first_search(data, i, visited)
    return

data = {
    'A': {'B'},
    'B': {'A', 'C', 'D'},
    'C': {'B', 'E'},
    'D': {'B', 'E'},
    'E': {'C', 'D', 'F'},
    'F': {'E'}
}

if __name__ == '__main__':
    depth_first_search(data, 'F')