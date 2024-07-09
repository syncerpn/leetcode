# dont even need stack
class Solution:
    def maxDepth(self, s: str) -> int:
        d = 0
        d_max = 0
        for c in s:
            if c == "(":
                d += 1
                d_max = max(d_max, d)
            elif c == ")":
                d -= 1
        
        return d_max