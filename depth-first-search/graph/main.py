""" 
Depth First Search on graph to find a target value.

Example 1:
    Input: 
        graph = [[2,3,8],[1,7],[1,4,5],[2,6]]
        target = 1
    Output: 1
"""
def dfs_search(graph, target, start=0):
    visited = set()

    def dfs_helper(node):
        visited.add(node)
        
        if node == target:
            return True
            
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs_helper(neighbor):
                    return True

        return False

    return dfs_helper(start)

print(dfs_search([[2,3,8],[1,7],[1,4,5],[2,6]], 1))