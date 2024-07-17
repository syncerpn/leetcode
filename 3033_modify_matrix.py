# easy, modify in-place
class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        col_max = [max(p) for p in zip(*matrix)]
        for j in range(len(matrix[0])):
            for i in range(len(matrix)):
                if matrix[i][j] == -1:
                    matrix[i][j] = col_max[j]
        return matrix