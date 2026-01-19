# prefix sum
# bottom-right - bottom-left (if any) - top-right (if any) + top-left (if any)
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(1, n):
                mat[i][j] += mat[i][j-1]
        
        for j in range(n):
            for i in range(1, m):
                mat[i][j] += mat[i-1][j]
        
        for k in range(min(n,m)-1, -1, -1):
            for i in range(m-k):
                for j in range(n-k):
                    s = mat[i+k][j+k]
                    if i > 0:
                        s -= mat[i-1][j+k]
                    if j > 0:
                        s -= mat[i+k][j-1]
                    if i > 0 and j > 0:
                        s += mat[i-1][j-1]
                    if s <= threshold:
                        return k + 1
        
        return 0

# can be faster with binary search instead of linear searching k
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(1, n):
                mat[i][j] += mat[i][j-1]
        
        for j in range(n):
            for i in range(1, m):
                mat[i][j] += mat[i-1][j]
        
        def is_valid(k):
            for i in range(m-k):
                for j in range(n-k):
                    s = mat[i+k][j+k]
                    if i > 0:
                        s -= mat[i-1][j+k]
                    if j > 0:
                        s -= mat[i+k][j-1]
                    if i > 0 and j > 0:
                        s += mat[i-1][j-1]
                    if s <= threshold:
                        return True
            
            return False
        
        l, r = 0, min(m, n)
        ans = 0
        while l <= r:
            k = (l + r) // 2
            if is_valid(k):
                l = k + 1
                ans = k
            else:
                r = k - 1
        
        return l