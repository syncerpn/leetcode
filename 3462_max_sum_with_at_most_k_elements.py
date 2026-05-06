# easy oneline
class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        return sum(sorted(sum([sorted(g, reverse=True)[:l] for g, l in zip(grid, limits)], start=[]), reverse=True)[:k])