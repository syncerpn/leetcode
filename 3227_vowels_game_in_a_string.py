# easy
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        V = set(list("aeiou"))
        ans = sum(c in V for c in s)
        return ans > 0