# just find intersection of two list
# mins of rows and maxs of cols
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        row_min = set(map(min, matrix))
        col_max = set([max([matrix[i][j] for i in range(m)]) for j in range(n)])
        return row_min.intersection(col_max)
