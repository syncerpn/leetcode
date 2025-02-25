# constant space dp
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        se, so = 0, 0
        ans = 0
        for a in arr:
            if a % 2:
                so, se = se + 1, so
            else:
                se = se + 1
            ans = (ans + so) % MOD
        
        return ans