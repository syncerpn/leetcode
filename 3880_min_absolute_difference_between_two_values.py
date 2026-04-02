# easy
class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        p, q = -1, -1
        ans = float("inf")
        for i, a in enumerate(nums):
            if a == 1:
                p = i
            elif a == 2:
                q = i
            
            if p >= 0 and q >= 0:
                ans = min(ans, abs(p - q))
        
        return ans if ans < float("inf") else -1