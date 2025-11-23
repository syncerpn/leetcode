# easy
class Solution:
    def minimumFlips(self, n: int) -> int:
        s = bin(n)[2:]
        k = len(s)
        ans = 0
        for i in range(k // 2):
            ans += 2 * (s[i] != s[~i])
        return ans
