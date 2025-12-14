# easy hard
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10 ** 9 + 7
        s = corridor.count("S")
        if s == 0 or s % 2:
            return 0
        ans = 1
        corridor = corridor.strip("P")
        s, p = 0, 1
        for c in corridor:
            if c == "S":
                if s == 0:
                    ans = (ans * p) % MOD
                    p = 0
                s = (s + 1) % 2
            if s == 0:
                p += 1
        return ans