# utilize set
class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        s = sorted(list(set(nums)))
        if len(s) > 2:
            return s[1]
        else:
            return -1