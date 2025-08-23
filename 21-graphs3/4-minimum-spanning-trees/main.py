# Prim's Algorithm for MST - Python Example

import heapq

def prim_mst(graph):
    start = 0
    mst_set = set()
    min_heap = [(0, start, -1)]  # (weight, vertex, parent)
    mst_edges = []
    total_weight = 0

    while min_heap and len(mst_set) < len(graph):
        weight, vertex, parent = heapq.heappop(min_heap)
        if vertex in mst_set:
            continue
        mst_set.add(vertex)
        if parent != -1:
            mst_edges.append((parent, vertex, weight))
            total_weight += weight
        for to, w in graph[vertex]:
            if to not in mst_set:
                heapq.heappush(min_heap, (w, to, vertex))
    return mst_edges, total_weight

graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8)],
    4: [(1, 5), (2, 7)]
}

edges, weight = prim_mst(graph)
print("Edges in MST:", edges)
print("Total weight of MST:", weight)
