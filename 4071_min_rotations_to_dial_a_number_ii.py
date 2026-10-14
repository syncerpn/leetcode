# easy
class Solution:
    def minRotations(self, n: int, s: str) -> int:
        ans = 0
        p = 0
        dp = [0]
        for c in s:
            c = int(c)
            a, b = min(p, c), max(p, c)
            ans += min(b - a, a + 10 - b)
            p = c
            dp.append(ans)
        c = 0
        p = int(s[-1])
        for k in range(n):
            a, b = min(p, c), max(p, c)
            ans = min(ans, min(b - a, a + 10 - b) + dp[k] + dp[n] - dp[k+1])
            c = int(s[k])
        return ans

# can also reduce to O(1) space
class Solution:
    def minRotations(self, n: int, s: str) -> int:
        ans = 0
        p = 0
        for c in s:
            c = int(c)
            a, b = min(p, c), max(p, c)
            ans += min(b - a, a + 10 - b)
            p = c
        t = ans
        p = 0
        q = int(s[-1])

        for k in range(n):
            c = int(s[k])
            a, b = min(p, c), max(p, c)
            x = min(b - a, a + 10 - b)
            a, b = min(p, q), max(p, q)
            y = min(b - a, a + 10 - b)
            ans = min(ans, t + y - x)
            p = c
        return ans
