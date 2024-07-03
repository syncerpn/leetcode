# we dont need to simulate the increment
# just store the information row-based and col-based
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        dr = [0] * m
        dc = [0] * n
        for ri, ci in indices:
            dr[ri] += 1
            dc[ci] += 1
        a = 0
        for ri in range(m):
            for ci in range(n):
                if (dr[ri] + dc[ci]) % 2 == 1:
                    a += 1
        
        return a