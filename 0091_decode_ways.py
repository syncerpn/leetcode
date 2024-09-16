# dp
# solved it and boosted a lot more confidence
class Solution:
    def numDecodings(self, s: str) -> int:
        single = set([str(i) for i in range( 1,10)])
        double = set([str(i) for i in range(10,27)])
        n = len(s)
        dp = [0] * n
        for i, c in enumerate(s):
            if c in single:
                if i == 0:
                    dp[i] += 1
                else:
                    dp[i] += dp[i-1]
            if i >= 1 and (s[i-1] + c) in double:
                if i == 1:
                    dp[i] += 1
                else:
                    dp[i] += dp[i-2]
        return dp[n-1]