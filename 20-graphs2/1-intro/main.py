# Advanced Graph Algorithms Introduction - Python Example

graph = {
    0: [1, 2],
    1: [0],
    2: [0, 3],
    3: [10]
}

print("Graph vertices:", list(graph.keys()))
print("Graph edges from 0:", graph)
