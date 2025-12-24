# dp
# up to i, what is the max length of subsequence to append i-th char to
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m, n = len(strs), len(strs[0])
        dp = [1] * n
        for i in range(1, n):
            for k in range(i):
                for j in range(m):
                    if strs[j][i] < strs[j][k]:
                        break
                else:
                    dp[i] = max(dp[i], dp[k] + 1)
        
        return n - max(dp)