"""
Belllman Ford Algorithm
"""
def bellman_ford(graph, source):
    """
    Finds the shortest paths from a source vertex to all other vertices in a graph.

    Args:
      graph: A dictionary representing the graph, where keys are vertices and values are lists of tuples (neighbor, weight).
      source: The source vertex.

    Returns:
      A tuple containing:
        - distances: A dictionary of shortest distances from the source to each vertex.
        - predecessors: A dictionary of predecessors for each vertex in the shortest paths.
        - negative_cycle: A boolean indicating if a negative cycle exists.
    """
    distances = {vertex: float('inf') for vertex in graph}
    distances[source] = 0
    predecessors = {vertex: None for vertex in graph}
    negative_cycle = False

    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbor, weight in graph[vertex]:
                if distances[vertex] + weight < distances[neighbor]:
                    distances[neighbor] = distances[vertex] + weight
                    predecessors[neighbor] = vertex

    for vertex in graph:
        for neighbor, weight in graph[vertex]:
            if distances[vertex] + weight < distances[neighbor]:
                negative_cycle = True
                break
        if negative_cycle:
            break
    return distances, predecessors, negative_cycle

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 3)],
    'C': [('D', 2), ('E', 5)],
    'D': [('E', 1)],
    'E': [('F', 3)],
    'F': []
}

distances, predecessors, negative_cycle = bellman_ford(graph, 'A')
print("Distances:", distances)
print("Predecessors:", predecessors)
print("Negative Cycle:", negative_cycle)