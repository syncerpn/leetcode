# easy
class Solution:
    def maxValue(self, n: str, x: int) -> str:
        if n[0] == "-":
            for i, c in enumerate(n):
                if i == 0:
                    continue
                if int(c) > x:
                    return n[:i] + str(x) + n[i:]
        else:
            for i, c in enumerate(n):
                if int(c) < x:
                    return n[:i] + str(x) + n[i:]
        return n + str(x)