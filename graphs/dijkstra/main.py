""" 
Dijkstra Algorithm
"""
import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example Usage
if __name__ == '__main__':
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 5, 'C': 1},
        'C': {'D': 8, 'E': 10},
        'D': {'E': 2, 'F': 6},
        'E': {'F': 3},
        'F': {}
    }

    start_node = 'A'
    shortest_distances = dijkstra(graph, start_node)
    print(f"Shortest distances from {start_node}: {shortest_distances}")
