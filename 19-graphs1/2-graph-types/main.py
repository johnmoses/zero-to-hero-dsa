# Graph Types - Python Example

# Directed Graph
directed_graph = {
    "A": ["B"],
    "B": ["C"],
    "C": []
}

# Weighted Graph (undirected)
weighted_graph = {
    "A": [("B", 4), ("C", 3)],
    "B": [("A", 4), ("C", 1)],
    "C": [("A", 3), ("B", 1)]
}

print("Directed graph edges from A:", directed_graph["A"])
print("Weighted edges from A:", weighted_graph["A"])
