# surprisingly easy
class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        ans = 0
        m = 0
        for a in nums:
            if a >= m:
                m = a
                ans += 1
        return ans