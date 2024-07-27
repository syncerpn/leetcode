# iterative row by row, top-down
# for each row index i, we find the tower of consecutive 1s from i to 0 (bottom-up)
# then sort the towers by their heights and count the rectangle area
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        s = [0] * n
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    s[j] = 0
                else:
                    s[j] += 1
            m = sorted(s, reverse=True)
            for j in range(n):
                if m[j] == 0:
                    break
                ans = max(ans, m[j] * (j+1))
        
        return ans