""" 
Redundant Connection

In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

Example 1:

Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Example 2:

Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
"""
def findRedundantConnection(edges):
    parent = [i for i in range(len(edges) + 1)]
    rank = [1] * (len(edges) + 1)

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        xr, yr = find(x), find(y)
        if xr == yr:
            return False
        if rank[xr] > rank[yr]:
            xr, yr = yr, xr
        parent[yr] = xr
        if rank[xr] == rank[yr]:
            rank[xr] += 1
        return True

    for x, y in edges:
        if not union(x, y):
            return [x, y]
    return []

print(findRedundantConnection([[1,2],[1,3],[2,3]]))