# not that hard, should know that it is dp right away
# yet need to revisit for implementation
# also python shows its weak point
# that needs quite a few tricks to not become tle
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        NEG = -(1 << 63)
        n, m = len(nums1), len(nums2)
        dp = [[[NEG for _ in range(k+1)] for _ in range(m+1)] for _ in range(n+1)]

        dp[0][0][0] = 0

        for i in range(n+1):
            for j in range(m+1):
                for t in range(k+1):
                    if i > 0:
                        dp[i][j][t] = max(dp[i][j][t], dp[i-1][j][t])
                    if j > 0:
                        dp[i][j][t] = max(dp[i][j][t], dp[i][j-1][t])
                    if i > 0 and j > 0 and t > 0 and dp[i-1][j-1][t-1] != NEG:
                        dp[i][j][t] = max(dp[i][j][t], dp[i-1][j-1][t-1] + nums1[i-1] * nums2[j-1])
        
        return dp[n][m][k]