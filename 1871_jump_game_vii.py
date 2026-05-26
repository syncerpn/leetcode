# line sweep solution is fun
# at a point, you may jump to any "0" in a segment
# so we can form the segment using line sweep
# at the end, check whether the last index is within a segment
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] != "0":
            return False
        n = len(s)
        d = [0] * (n + 1)
        p = 0
        d[0] += 1
        d[1] -= 1
        for i, c in enumerate(s):
            p += d[i]
            if p > 0 and c == "0":
                j = i + minJump
                if j < n:
                    d[j] += 1
                    j = min(i + maxJump + 1, n)
                    d[j] -= 1
        return p > 0