# easy
class Solution:
    def removeZeros(self, n: int) -> int:
        ans = ""
        s = str(n)
        for c in s:
            if c != "0":
                ans += c
        return int(ans)