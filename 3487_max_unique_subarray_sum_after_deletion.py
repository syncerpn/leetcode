# cases where s contains only negatives tricked me
# lol, actually good question
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        s = set(nums)
        if max(s) >= 0:
            return sum(a for a in s if a >= 0)
        return max(s)