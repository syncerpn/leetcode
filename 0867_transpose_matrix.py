# one-liner, col first traversal
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [[matrix[mi][ni] for mi in range(len(matrix))] for ni in range(len(matrix[0]))]

# even cleaner using zip
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return list(zip(*matrix))