# greedy
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        p = 0
        ans = 0
        for a in nums:
            p += a
            if p > 0:
                ans += 1
        return ans