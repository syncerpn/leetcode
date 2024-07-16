# likely max pooling
# which is too familiar to me
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        result = [[0 for _ in range(n-2)] for _ in range(n-2)]
        for i in range(n-2):
            for j in range(n-2):
                result[i][j] = max([max(grid[k][j:j+3]) for k in range(i,i+3)])
        
        return result