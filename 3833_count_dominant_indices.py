# easy
class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        s, n = sum(nums), len(nums)
        ans = 0
        for a in nums:
            n -= 1
            s -= a
            if n and a > s / n:
                ans += 1
        return ans