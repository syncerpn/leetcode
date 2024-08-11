# seems hard at the first glance
# but it is actually pretty easy
# because we need at most 2 days
# so we need to check 3 cases
# 1. the grid initially has 0 or > 1 islands, return 0 because it is already disconnected
# 2. try replacing each land cell with water and check if we can split the island, then return 1
# 3. otherwise, we need 2 days
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        v = set((i, j) for i in range(m) for j in range(n) if grid[i][j])
        
        def dfs(v):
            islands = []
            while v:
                s = [v.pop()]
                d = []
                while s:
                    x, y = s.pop()
                    d.append((x, y))
                    for p in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                        if p in v:
                            s.append(p)
                            v.discard(p)
                islands.append(d)
            return islands
        
        islands = dfs(v)
        if len(islands) != 1:
            return 0
        
        island = islands[0]
        for p in island:
            v = set(island)
            v.discard(p)
            if len(dfs(v)) != 1:
                return 1
        return 2