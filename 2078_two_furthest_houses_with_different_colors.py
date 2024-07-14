# one of two ends should be use to calculate max distance
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        d = 0
        for i, c in enumerate(colors):
            if c != colors[0]:
                d = max(d, i)
            if c != colors[-1]:
                d = max(d, len(colors) - 1 - i)
        return d