# Dijkstra's Algorithm - Python Example

import heapq

def dijkstra(graph, start):
    heap = [(0, start)]
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    while heap:
        current_dist, current_vertex = heapq.heappop(heap)

        if current_dist > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

distances = dijkstra(graph, 'A')
print("Shortest distances from A:", distances)
