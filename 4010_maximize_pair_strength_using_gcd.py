# brute-force version
class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        ans = 0
        for a in nums:
            for b in nums:
                d = gcd(a, b)
                ans = max(ans, a * b // d // d)
        
        return ans

