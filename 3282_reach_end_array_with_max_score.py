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