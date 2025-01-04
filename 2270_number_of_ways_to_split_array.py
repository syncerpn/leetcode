# easy
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        s = sum(nums)
        t = 0
        ans = 0
        for i in range(len(nums)-1):
            t += nums[i]
            if t >= s - t:
                ans += 1
        return ans