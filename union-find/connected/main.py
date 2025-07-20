""" 
Connected
"""


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)

        if root_x != root_y:
            # Union by rank
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

            self.components -= 1
            return True
        return False

    def connected(self, x, y):
        return self.find(x) == self.find(y)

def number_of_islands(grid):
    if not grid:
        return 0
    
    m, n = len(grid), len(grid[0])
    uf = UnionFind(m * n)
    islands = 0
    
    def get_index(i, j):
        return i * n + j
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                islands += 1
                
                # Check neighbors
                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ni, nj = i + di, j + dj
                    if (0 <= ni < m and 0 <= nj < n and 
                        grid[ni][nj] == '1'):
                        if uf.union(get_index(i, j), get_index(ni, nj)):
                            islands -= 1
    
    return islands

def accounts_merge(accounts):
    uf = UnionFind(len(accounts))
    email_to_id = {}
    
    # Map emails to account IDs
    for i, account in enumerate(accounts):
        for email in account[1:]:
            if email in email_to_id:
                uf.union(i, email_to_id[email])
            else:
                email_to_id[email] = i
    
    # Group emails by root account
    groups = {}
    for email, account_id in email_to_id.items():
        root = uf.find(account_id)
        if root not in groups:
            groups[root] = []
        groups[root].append(email)
    
    # Format result
    result = []
    for root, emails in groups.items():
        name = accounts[root][0]
        result.append([name] + sorted(emails))
    
    return result

print(accounts_merge([["John", "zTt2G@example.com", "V2YsF@example.com"], ["John", "zTt2G@example.com", "zTt2G@example.com"], ["Mary", "V2YsF@example.com"], ["John", "h2BpV@example.com"]]))
