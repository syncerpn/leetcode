# easy
class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        mis = [nums[-1]]
        n = len(nums)
        for i in range(n-2, 0, -1):
            mis.append(min(mis[-1], nums[i]))
        
        ans = -float("inf")
        p = 0
        for i in range(n-1):
            p += nums[i]
            ans = max(ans, p - mis.pop())
        return ans