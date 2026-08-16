# just try all
class Solution:
    def minOperations(self, s: str) -> int:
        ans = inf
        n = len(s)
        for i in range(n):
            cur = i
            for j in range(n // 2):
                a = ord(s[(i + j) % n])
                b = ord(s[(i - j - 1) % n])
                d = abs(a - b)
                cur += min(d, 26 - d)
                if cur > ans:
                    break
            ans = min(ans, cur)
        return ans