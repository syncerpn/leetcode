# manacher's algorithm O(n)
class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) <= 1:
            return 1
        
        s = '#' + '#'.join(s) + '#'
        dp = [0 for _ in range(len(s))]
        center = 0
        right = 0
        ans = 0
        for i in range(len(s)):
            if i < right:
                dp[i] = min(right-i, dp[2*center-i])
            while i-dp[i]-1 >= 0 and i+dp[i]+1 < len(s) and s[i-dp[i]-1] == s[i+dp[i]+1]:
                dp[i] += 1
            ans += (dp[i] + 1) // 2
            if i+dp[i] > right:
                center = i
                right = i+dp[i]
        return ans