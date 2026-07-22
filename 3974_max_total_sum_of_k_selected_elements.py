# greedy
class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        nums.sort()
        i = -1
        ans = 0
        for i in range(k):
            if mul > 1:
                ans += nums[~i] * mul
            else:
                ans += nums[~i]
            mul -= 1
        return ans

