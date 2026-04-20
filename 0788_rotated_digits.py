# easy
class Solution:
    def rotatedDigits(self, n: int) -> int:
        V = {"2", "5", "6", "9"}
        Q = {"3", "4", "7"}
        ans = 0
        for a in range(1, n+1):
            s = str(a)
            v = False
            for c in s:
                if c in Q:
                    break
                if c in V:
                    v = True
            else:
                ans += int(v)

        return ans