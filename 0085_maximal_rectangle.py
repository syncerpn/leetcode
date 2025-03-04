# my solution which use dp prefix sum rows and cols
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        rows = []
        cols = []
        for i in range(m):
            t = 0
            d = []
            for j in range(n):
                if matrix[i][j] == "1":
                    t += 1
                else:
                    t = 0
                d.append(t)
            rows.append(d)
        
        for j in range(n):
            t = 0
            d = []
            for i in range(m):
                if matrix[i][j] == "1":
                    t += 1
                else:
                    t = 0
                d.append(t)
            cols.append(d)
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0":
                    continue
                r = rows[i][j]
                for k in range(cols[j][i]):
                    r = min(r, rows[i-k][j])
                    ans = max(ans, (k+1) * r)

        return ans

# better dp with the same concept as in #0084
# using monostack
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def hist(heights):
            s = [-1]
            heights.append(0)
            a = 0
            for i in range(len(heights)):
                while heights[i] < heights[s[-1]]:
                    hj = heights[s.pop()]
                    wj = i - s[-1] - 1
                    a = max(a, hj*wj)
                s.append(i)
            return a

        m, n = len(matrix), len(matrix[0])
        row = [0] * n
        ans = 0
        for i in range(m):
            for j in range(n):
                row[j] = 0 if matrix[i][j] == "0" else row[j] + 1
            print(row)
            ans = max(ans, hist(row))
        
        return ans