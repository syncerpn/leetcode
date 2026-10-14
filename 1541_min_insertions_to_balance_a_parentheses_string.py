# quite easy, but a bit non-trivial
class Solution:
    def minInsertions(self, s: str) -> int:
        ans = 0
        b = 0
        for c in s:
            if c == "(":
                if b == -1:
                    ans += 2
                    b = 0
                elif b % 2:
                    ans += 1
                    b -= 1
                b += 2
            else:
                b -= 1
            if b == -2:
                ans += 1
                b = 0
        if b == -1:
            ans += 2
            b = 0
        elif b % 2:
            ans += 1
            b -= 1
        return ans + b