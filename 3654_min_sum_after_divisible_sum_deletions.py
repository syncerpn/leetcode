# dp, prefix sum
# messed up indexing so hard i ranked 4k this time :(
class Solution:
    def minArraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s = [0]
        d = {0: -1}
        dp = [0] * (n + 1)
        for i, a in enumerate(nums):
            s.append(s[-1] + a)
            p = s[-1] % k
            if p not in d:
                dp[i+1] = dp[i]
            else:
                j = d[p]
                dp[i+1] = max(dp[i], dp[j+1] + s[i+1] - s[j+1])
            d[p] = i
        return s[-1] - dp[-1]