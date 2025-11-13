# greedy, from left to right
class Solution:
    def maxOperations(self, s: str) -> int:
        s += "1"
        p = 0
        z = False
        ans = 0
        for c in s:
            if c == "0":
                if not z:
                    z = True
            else:
                if z:
                    ans += p
                z = False
                p += 1
        return ans

