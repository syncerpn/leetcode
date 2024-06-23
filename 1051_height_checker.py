# sort and check for general constraints
# counting sort might be used in specific cases
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sheights = sorted(heights)
        c = 0
        for s, h in zip(sheights, heights):
            c += (s != h)
        return c