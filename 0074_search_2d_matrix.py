# binary search
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = bisect.bisect([m[0] for m in matrix], target)
        if i <= 0:
            return False
        j = bisect.bisect(matrix[i-1], target)
        return j > 0 and matrix[i-1][j-1] == target