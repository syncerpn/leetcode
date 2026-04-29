# just try all cases
class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        return max(["%d%d:%d%d" % t for t in itertools.permutations(arr) if t[:2] < (2, 4) and t[2] < 6] or [""])