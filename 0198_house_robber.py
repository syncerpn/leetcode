# O(1) space is enough
# simple dp with
# 1. did you rob the last house (dp_1) -> skip this one
# 2. or did you skip the last house (dp_0) -> rob this one
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp_0 = dp_1 = 0
        for n in nums:
            dp_0, dp_1 = dp_1, max(dp_1, dp_0 + n)
        return max(dp_0, dp_1)