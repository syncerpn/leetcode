# this is my dp which is O(n2)
# obviously the logic is flawless, yet gave me tle
# because simply, we dont even need dp if we know math
class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        for i in range(1, n):
            for j in range(i):
                dp[i] = max(dp[i], dp[j] + nums[j] * (i - j))
        return dp[-1]

# greedy just works like a magic
# math definitely is important to optimize your shit
# and i suck at math this time...
class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        s = []
        n = len(nums)
        ans = 0
        for i, ni in enumerate(nums[:-1]):
            if not s:
                s.append((i, ni))
            else:
                j, nj = s[-1]
                if ni > nj:
                    ans += (i - j) * nj
                    s.append((i, ni))
        
        i, ni = s[-1]
        ans += (n-1 - i) * ni
        return ans

# best explanation with dp (by ye15)
# Providing an alternative view via dp which I believe is more straightforward to understand.
# Define dp[i] as the maximum score ending at i. Boundary condition is dp[0] == 0 and dp[-1] gives the answer.
# dp[1] = dp[0] + nums[0]
# dp[2] = max(dp[0]+2*nums[0], dp[1]+nums[1]) = max(dp[1]+nums[0], dp[1]+nums[1]) = dp[1] + max(nums[0], nums[1])
# dp[3] = max(dp[0]+3*nums[0], dp[1]+2*nums[1], dp[2]+nums[2]) = max(dp[1]+2*max(nums[0], nums[1]), dp[2]+nums[2])=max(dp[2]+max(nums[0], nums[1]), dp[2]+nums[2]) = dp[2]+max(nums[0], nums[1], nums[2])
# This goes on... namely,