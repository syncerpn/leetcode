# top-down
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            n = len(triangle[i])
            for j in range(0, n):
                triangle[i][j] = triangle[i][j] + min(triangle[i-1][max(0,j-1)], triangle[i-1][min(j,n-2)])
        
        return min(triangle[-1])

# or bottom-up
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        for i in range(m-2,-1,-1):
            n = len(triangle[i])
            for j in range(n):
                triangle[i][j] = triangle[i][j] + min(triangle[i+1][j], triangle[i+1][j+1])
        
        return triangle[0][0]