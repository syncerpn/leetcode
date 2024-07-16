# sort and take the max of each
# because they line up after sorting
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for g in grid:
            g.sort()
        return sum([max(p) for p in zip(*grid)])