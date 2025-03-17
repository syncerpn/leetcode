# dp
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        nums.sort()
        for a in range(1, target+1):
            for b in nums:
                if b > a:
                    break
                dp[a] += dp[a-b]
        
        return dp[target]