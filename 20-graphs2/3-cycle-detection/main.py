# Cycle Detection in Directed Graph - Python Example

def is_cyclic_util(graph, v, visited, rec_stack):
    visited.add(v)
    rec_stack.add(v)

    for neighbor in graph.get(v, []):
        if neighbor not in visited:
            if is_cyclic_util(graph, neighbor, visited, rec_stack):
                return True
        elif neighbor in rec_stack:
            return True

    rec_stack.remove(v)
    return False

def is_cyclic(graph):
    visited = set()
    rec_stack = set()

    for node in graph.keys():
        if node not in visited:
            if is_cyclic_util(graph, node, visited, rec_stack):
                return True
    return False

# Example directed graph with cycle
graph = {
    0: [1],
    1: [10],
    2: [0, 3],  
    }

print("Graph contains cycle:", is_cyclic(graph))
