# fairly easy
class Solution:
    def minFlips(self, target: str) -> int:
        n = 0
        p = "0"
        for c in target:
            if c == "1" and p == "0":
                n += 1
            p = c
        return n * 2 - (p == "1")