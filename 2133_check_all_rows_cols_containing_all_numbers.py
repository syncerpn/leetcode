# check with set
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        rows = [len(set(m)) == n for m in matrix]
        if not all(rows):
            return False
        cols = [len(set(m)) == n for m in zip(*matrix)]
        return all(cols)