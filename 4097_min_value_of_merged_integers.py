# easy
class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        ans = inf
        for i in range(len(nums)//2):
            a = nums[2*i]
            b = nums[2*i+1]
            ans = min(ans, a * (10 ** len(str(b))) + b)
        return ans