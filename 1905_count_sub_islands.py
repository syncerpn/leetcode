# find all islands in grid2
# it should be a subisland if every land on the found island in grid2 is also a land in grid1
# in short, we will just use grid1 as the reference check for subisland
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])
        v = set([(i, j) for j in range(n) for i in range(m) if grid2[i][j]])
        
        ans = 0
        while v:
            i, j = v.pop()
            is_subisland = grid1[i][j]
            s = [(i, j)]
            while s:
                r, c = s.pop()
                for i, j in [(r+1, c), (r-1,c), (r, c+1), (r, c-1)]:
                    if 0 <= i < m and 0 <= j < n and (i, j) in v:
                        if grid1[i][j] == 0:
                            is_subisland = 0
                        s.append((i, j))
                        v.discard((i, j))
            ans += is_subisland
        return ans