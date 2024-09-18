# 2d dp
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}
        for n in nums:
            dp_next = {}
            for k in dp:
                if k-n not in dp_next:
                    dp_next[k-n] = 0
                dp_next[k-n] += dp[k]

                if k + n not in dp_next:
                    dp_next[k+n] = 0
                dp_next[k+n] += dp[k]
            
            dp = dp_next

        return dp[target] if target in dp else 0