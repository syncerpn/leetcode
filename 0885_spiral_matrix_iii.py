# going spiral makes me feel dizzy
# we extend left 1, down 1, right 2, up 2, left 3, down 3, right 4, down 4
# you see the pattern, right?
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        i, j = rStart, cStart
        l = 1
        v = 1
        d = [(0,1), (1,0), (0,-1), (-1,0)]
        t = 0
        ans = []
        k = 1
        while k <= rows * cols:
            if 0 <= i < rows and 0 <= j < cols:
                ans.append([i, j])
                k += 1
            
            x, y = d[t]
            i, j = i + x, j + y

            v -= 1
            if v == 0:
                v = l
                t = (t + 1) % 4
                if t == 1 or t == 3:
                    l += 1            

        return ans