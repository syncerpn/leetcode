# was overthinking this one
# the mat contains complete information
# was thinking about union-find with incomplete mat
class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        return max([(sum(p), i) for i, p in enumerate(grid)])[1]