# parentheses and stack are best friend
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        r = 0
        p = []
        for c in s:
            if c == ")":
                if not p:
                    r += 1
                else:
                    p.pop()
            else:
                p.append(c)
        
        r += len(p)
        return r
            