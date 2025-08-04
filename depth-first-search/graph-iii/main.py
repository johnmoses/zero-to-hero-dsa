""" 
Depth First Search on graph to find a target value.

Example 1:
    Input: 
        graph = [[2,3,8],[1,7],[1,4,5],[2,6]]
        target = 1
    Output: 1
"""
def dfs(graph, target, start=0):
    visited = set()

    def helper(node):
        visited.add(node)
        
        if node == target:
            return True
            
        for i in graph[node]:
            if i not in visited:
                if helper(i):
                    return True

        return False

    return helper(start)

print(dfs([[2,3,8],[1,7],[1,4,5],[2,6]], 1))