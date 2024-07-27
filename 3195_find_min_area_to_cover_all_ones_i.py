# sweep left right then up down
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rs = 0
        while rs < m:
            if sum(grid[rs]) > 0:
                break
            rs += 1
        
        re = m - 1
        while re >= rs:
            if sum(grid[re]) > 0:
                break
            re -= 1
        
        grid = list(zip(*grid))
        cs = 0
        while cs < n:
            if sum(grid[cs]) > 0:
                break
            cs += 1
        
        ce = n - 1
        while ce >= cs:
            if sum(grid[ce]) > 0:
                break
            ce -= 1
        return (ce - cs + 1) * (re - rs + 1)