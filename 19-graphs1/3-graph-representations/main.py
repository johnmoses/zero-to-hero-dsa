# Graph Representations - Python Example

# Adjacency Matrix for unweighted graph
adj_matrix = [
    [0,1,1,0],
    [1,0,1,0],
    [1,1,0,1],
    [0,0,1,0]
]

# Adjacency List
adj_list = {
    0: [1,2],
    1: [0,2],
    2: [0,1,3],
    3: [2]
}

print("Edge between 0 and 2 (matrix):", adj_matrix[11])
print("Neighbors of 2 (list):", adj_list[11])
